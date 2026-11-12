def outside_completion(self, messages: list[Any], stream: bool = False,
                       tools: list[Any] = None) -> ChatTextResponse | list[
    ChatToolsResponse]:
    # 需要自己实现function calling功能，自己解析返回内容。留意think标签，深度思考模型必定返回think标签，所以最好把function calling识别结果
    # 放到<tools_call>标签中。可以一次返回多个工具调用
    # 如果有tools就把tools的提示词和tools拼接到role:system的提示词里面。
    # 后面根据输出格式进行解析
    tool_call_regex = r'<toolCall>'
    # 定义正则表达式，匹配 <toolCall> 和 </toolCall> 之间的内容
    tool_call_full_match_regex = r'<toolCall>(.*?)</toolCall>'

    outside_body = {
        "messages": messages,
        "mode": self.setting.model,
        "temperature": self.setting.temperature,
        "stream": stream
    }
    completion = http_post_outside(outside_body)
    if stream:
        full_reply = ''
        for chunk in completion:
            # 校验是否存在工具调用，如果前面是think标签或其他内容，就直接返回文本块。遇到<tools_call>标签就返回工具调用
            print(chunk)
            if chunk != '[DONE]':
                full_reply += chunk
                matched = None
                if tools is not None:
                    matched = re.match(tool_call_regex, full_reply)
                if matched:
                    # 判断是否包含函数开始标记
                    # 查找匹配结果（re.DOTALL 确保 .*? 匹配换行符）
                    match = re.search(tool_call_full_match_regex, full_reply, re.DOTALL)
                    if match:
                        # 提取标签内的内容
                        tool_content = match.group(1).strip()  # strip() 去除首尾空白
                        tool_content = tool_content.replace('```json', '').replace('```', '')
                        tool_json = json.loads(tool_content)
                        tool_call_list = [ChatToolsResponse(type='function', function=ChatToolsFunction(
                            name=tool.get('function_name'), parameters=tool.get('parameters'))) for tool in
                                          tool_json]
                        yield tool_call_list
                        # 抛出工具调用信息
                        # 截取工具调用信息，抛出完整的工具调用信息，不用一段一段的抛出
                    else:
                        # 说明输出尚未结束，还没有工具结束标记
                        pass
                else:
                    yield ChatTextResponseChunk(
                        content=chunk,
                        type='text'
                    )
            else:
                return

    else:
        full_reply = completion.data
        # 校验是否存在工具调用, 使用正则截取toolCall标签中的内容，然后转成json
        match = None
        if tools is not None:
            match = re.search(tool_call_full_match_regex, full_reply, re.DOTALL)
        if match:
            # 提取标签内的内容
            tool_content = match.group(1).strip()  # strip() 去除首尾空白
            tool_content = tool_content.replace('```json', '').replace('```', '')
            tool_json = json.loads(tool_content)
            tool_call_list = [ChatToolsResponse(type='function',
                                                function=ChatToolsFunction(name=tool.get('function_name'),
                                                                           parameters=tool.get('parameters'))) for
                              tool in tool_json]
            return tool_call_list
        else:
            return ChatTextResponse(
                content=full_reply,
                type='text'
            )