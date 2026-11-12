# coding: utf-8
import asyncio
import json
import re

from core.mcp.client.mcp_client import McpClient
from model.mcp_management_model import MCPManagementModel
from util.httputil import http_post
from util.mcp_utils import MCPUtils

mcp_tool_guide = '''你是一个智能助手，能够根据用户需求判断是否需要调用工具。

## 行为准则
1. **合理判断**是否需要调用工具，避免不必要的重复调用
2. **工具返回异常或格式错误时**，可以重新调用或调整参数
3. **不要输出思考过程**，直接给出最终答案
4. **单次对话中**，相同目的的调用应避免重复

## 工具调用规则
- 仅当用户问题需要外部信息时才使用工具
- 工具调用格式：将JSON放在<toolCall></toolCall>标签内
- 工具调用示例：

<toolCall>
```json
[{"function_name": "tool_name", "parameters":{"param":"value"}}]
```
</toolCall>

## 合理重试场景
- ✅ 工具返回格式错误或异常时，可以调整参数重新调用
- ✅ 工具返回不完整信息时，可以补充调用获取更多信息
- ✅ 不同工具可针对同一问题的不同方面进行调用

## 避免场景
- ❌ 相同参数对同一工具的重复调用
- ❌ 已获取完整信息后无意义的再次调用
- ❌ 编造工具返回结果

## 回答格式
- 直接给出简洁准确的答案
- 基于工具返回的真实信息回答
- 不要提及工具调用过程
# 工具-Tools
## 输出工具的格式-ToolFormat
- 请结合前面的要求，严格输出JSON格式内容
- 文字内容提及需要使用工具列表中的工具时，在最后输出对应工具名的JSON格式内容
- 工具调用信息的JSON必须放在<toolCall></toolCall>标签中
- 工具调用时，输出单个工具调用的JSON格式，格式示例如下：
<toolCall>
```json
[{"function_name": "tool_A", "parameters":{"arg_name":"arg_value"}}]
```
</toolCall>
- 工具调用时，输出多个不同工具调用的JSON格式，格式示例如下：
<toolCall>
```json
[{"function_name": "tool_A", "parameters":{"arg_name":"arg_value"}}, {"function_name": "tool_B", "parameters":{"arg_name":"arg_value"}},...]
```
</toolCall>
- 请理解上述JSON格式定义，仅输出最终的JSON格式
- 输出的JSON的内容用双引号(""), 不要用单引号(")，并注意转义字符的使用
## 示例
可用工具示例如下：
- `deep_search`
```json
{"name": "deep_search", "description": "这是一个搜索工具，可以搜索各种互联网知识", "parameters": {"type": "object", "properties": {"query": {"description": "需要搜索的全部内容及描述", "type": "string"}}, "required": ["query"]}}
```
工具调用输出的示例格式如下：
<toolCall>
```json
[{"function_name": "deep_search", "parameters":{"query":"xxx"}}]
```
</toolCall>
## 约束
- 先输出文字内容，再输出工具调用的JSON格式
- 你只能能输出工具列表中的一个或多个，严禁输出工具列表中不存在的工具名
- 不要自行补充或者臆造内容
- 禁止输出多个相同入参的工具调用
## 工具列表 - Tool
有如下工具名和工具入参的介绍如下：
'''


async def _get_mcp_tools(mcp_client):
    """
    获取 MCP 工具列表
    """
    try:
        return await mcp_client.list_tools()
    except Exception as e:
        print(f"获取 MCP 工具列表失败: {str(e)}")
        return []


async def _call_mcp_tool(mcp_client, tool_name, arguments):
    """
    调用 MCP 工具
    """
    try:
        return await mcp_client.call_tool(tool_name, arguments)
    except Exception as e:
        print(f"调用 MCP 工具 {tool_name} 失败: {str(e)}")
        raise


def _need_call_mcp(response_data):
    """
    检查大模型是否要求调用 MCP 工具
    根据 <toolCall>...</toolCall> 标签判断
    """
    if isinstance(response_data, str):
        return "<toolcall>" in response_data.lower()
    return False


def _parse_mcp_call_request(response_data):
    """
    解析大模型返回的 MCP 调用请求
    提取 <toolCall>...</toolCall> 标签中的JSON内容
    """
    try:
        if isinstance(response_data, str):
            pattern = r'<toolCall>\s*```json\s*(.*?)\s*```\s*</toolCall>'
            match = re.search(pattern, response_data, re.DOTALL | re.IGNORECASE)

            if match:
                # 提取JSON字符串并解析
                json_str = match.group(1)
                tool_call = json.loads(json_str)
                return tool_call

        return None
    except Exception as e:
        print(f"解析 MCP 调用请求失败: {str(e)}")
        return None


def main():
    # 用户输入
    request_messages = [
        {
            "role": "user",
            "content": "我现位于河南郑州，今天天气怎么样？出门是否需要带伞？"
            # "content": "你好，怎么称呼你"
        }
    ]

    # 用户勾选了 mcp 服务就需要拼接系统提示词
    # 首先获取 MCP 工具列表
    try:
        test_sse_model = MCPManagementModel(
            id=1,
            name="test_sse_model",
            url="http://10.14.57.8:3003/sse",
            command="",
            protocol="sse",
            status="active",
            tags=["mcp"],
            timeout=5,
        )
        mcp_client = McpClient([test_sse_model])
        tools = MCPUtils.get_mcp_tools(mcp_client)
        tool_dicts = []
        for tool in tools:
            tool_info = {
                "name": tool.name,
                "description": tool.description,
                "inputSchema": tool.inputSchema
            }
            tool_dicts.append(tool_info)
        # 将工具列表转为JSON字符串拼接到系统提示词后，并放到用户输入message 之前
        # request_messages = [{"role": "system", "content": f"{mcp_tool_guide} {json.dumps(tool_dicts)}"}] + request_messages
        request_messages = [{"role": "system", "content": f"{mcp_tool_guide} 获取 MCP 工具列表失败"}] + request_messages
    except Exception as e:
        print(f"获取 MCP 工具列表失败: {str(e)}")
        request_messages = [{"role": "system", "content": f"{mcp_tool_guide} 获取 MCP 工具列表失败"}] + request_messages

    # 开始循环调用大模型
    max_mcp_calls = 6  # 设置最大调用次数，避免无限循环
    current_mcp_calls = 0
    response_msg = ""
    called_tools = {}  # 记录已调用过的工具及其参数，避免相同参数的重复调用
    # response_msg 为空或者 _need_call_mcp 返回 true 时，进入循环
    while (response_msg == "" or _need_call_mcp(response_msg)) and current_mcp_calls < max_mcp_calls:
        print(f"*** *** 当前 MCP 链式调用轮次: {current_mcp_calls}")
        current_mcp_calls += 1
        # 构建请求数据
        request_data = {
            "model": "qwen1.5-72b-chat",
            "temperature": 0.1,
            "messages": request_messages
        }
        print(f"<<< <<< 大模型输入: {request_data}")
        try:
            outside_list_url = "http://60.191.123.122:40273/se_outside/outSide/chat/chatCompletion"
            response = http_post(
                outside_list_url,
                body=request_data,
                headers={
                    "sign": "dGVzdA==",
                    "encrypt": "L3/K9PhDku+WSM0GSctZyAW9ACtablWEGCGZhCxW9our3JysQrjZlDPeQsA2ner8",
                    "Content-Type": "application/json"
                },
            )
            response.raise_for_status()
            # 判断大模型是否为流式输出
            # 如果为流式输出 pass
            # 如果为非流式输出， 能够直接获取 data
            response_msg = response.json()["data"]
            print(f">>> >>> 大模型输出: {response_msg}")
            # 如需继续调用 mcp
            if _need_call_mcp(response_msg):
                tool_calls = _parse_mcp_call_request(response_msg)
                # tool_call 的值取决于 system prompt 里定义的示例
                print(f"### ### 大模型要求调用 MCP 工具 tool_call: {tool_calls}")
                if tool_calls:
                    new_tool_called = False
                    for tool_call in tool_calls:
                        tool_name = tool_call["function_name"]
                        tool_params = json.dumps(tool_call["parameters"], sort_keys=True)
                        # 检查是否已调用过相同工具且参数相同
                        if tool_name in called_tools and called_tools[tool_name] == tool_params:
                            print(f"### ### 工具 {tool_name} 已用相同参数调用过，跳过重复调用")
                            continue
                        # 调用 MCP 工具
                        mcp_response = asyncio.run(
                            _call_mcp_tool(
                                mcp_client,
                                tool_name,
                                tool_call["parameters"]
                            )
                        )
                        called_tools[tool_name] = tool_params  # 记录已调用工具及参数
                        new_tool_called = True

                        # 添加上下文
                        request_messages.append({"role": "assistant", "tool_calls": tool_call})
                        # 提取 mcp_response 返回的 content
                        if mcp_response.content and len(mcp_response.content) > 0:
                            text_content = mcp_response.content[0].text
                            request_messages.append({"role": "tool", "name": tool_call["function_name"], "content": text_content})
                        else:
                            # 调用工具失败继续调用工具
                            request_messages.append({"role": "tool", "name": tool_call["function_name"], "content": str(mcp_response)})
                    # 只有当有新工具被调用时才继续循环
                    if new_tool_called:
                        continue
                # 如果没有新工具需要调用，结束循环
                break
            # 如无需调用 mcp 返回最终的回复
            else:
                return response_msg
        except Exception as e:
            raise RuntimeError(f"处理大模型请求时发生错误: {str(e)}")
    return None


if __name__ == '__main__':
    main()

