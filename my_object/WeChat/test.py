import requests


def main():

    cookies = {
        'TNU5z5PTPMUxS': '5ZKKTmA2ELvSwi2juTEkQppbROg.WVQqM7p_2fFU5dZf6Ew3g7AZVAEsCcJxUS_K_9CGqTd6qSMKygD.sLvYEnq',
        'yfx_c_g_u_id_10000005': '_ck22021422541316677813315517873',
        'yfx_f_l_v_t_10000005': 'f_t_1644850453656__r_t_1644850453656__v_t_1644850453656__r_c_0',
        'TNU5z5PTPMUxT': '53GNBnbEtQEZqqqm55W1XVAnZ_SUP0YulUeoMGCP0EjzPrP5lfQcOWqHgkTlAxNU80mTgsNJCOtAsB.Ys4Bj4t_q7V9sMOoNMSAaSAEFJNOv1SKuh_yvCbmosv5CqelMLFLZ5PuRUJgVQyjRSgHI6L0l1HWu6B8YkgQt9tLxMpA43_D770sqbUS47C6I1YxJoi0rmrnkNZGNiH5XujHcRM514EJQ8Up6ijyOnRgEM6iGP.WwWIklI67YaTS6k4lb8RLBtLEo1TTlGCbfhGdM77l',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://wwj.gansu.gov.cn/wwj/c105439/news_list.shtml',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8',
    }

    params = (
        ('FfNKEgqG',
         '589tgEVoS9FDeaS7W0nDVUpoEAUXepYZeMKaavX7FD6wYStAB1yBpiPb42FM17DO7Tsnc8PHPGdA8T7u.R0E9hKAhdfNxIMFI9tQZebU6TIpwCYtyYwKsCQ0Wop_PWjAdT5DT4gI9TmY6wNSyt.uDxukqeVXDTVNGx1OEX4Nxpswlj0euHokMgeAvzGNk1ghpzM__cqXuFtmmSCMNfkWw9Q0xggBnvAIa0oqRyoOabB142WdUANnZ.JWEhKAJAW2yQzj..hENenYaoLKP4FhOVoKawDZGWuLQAmGgRy2IKK4WckqxUEm0GU059yjr53V_'),
        ('0RQcg1Ab',
         '4cw1YoNuMXn30ziwkZ_Ggz9WRKRTiHzdm7zl07Ac71Z5N7sigAIrSTQU9G_UZmdsjGof5XUOAm9E_rUZBLOgsa5C.JqEobbhE2zfnn2Kea.0NatauxnsSlBeEm7xxDV_L9kMbewPgpmJbKbIfnsxE3R7K9N0fmiBY5xUe2336zQOGOK7DlFJqYnURT63DkF_JFe748bK5xGap1N52USRa9kDR7UEAwDzqrcT.yO1rdowX2Kproj1PoUwS5pImykM25uNGQ.GgYo2XMuF6kC7b0a'),
    )

    response = requests.get('http://wwj.gansu.gov.cn/common/search/0e77c906ca5843e88f17b3f0f3c03a5f', headers=headers, params=params, cookies=cookies, verify=False)

    print(response.text)
    print(response.status_code)


if __name__ == '__main__':
    main()

"""
http://wwj.gansu.gov.cn/common/search/0e77c906ca5843e88f17b3f0f3c03a5f?FfNKEgqG=5xP0QM.GOC4lGAz2ZpWXoX1spSpMmEPyCEEK2hL9stShVeB8bpAC1Wc8jgZD.kKifRiadbtU8RogVf_xm8RuHsQZChYsKnPbJS8QAmrW337RBsNRxP.jEr0UUx93MdyjLabe0.vqFLhrX8np3Wqch3e42ofAi9cNTeoSGETVde0vYwF.RIh5aXOIPIaK1Zjz4wbQm6MS6AD98NufKgAOZif10y.K.8mvsjHDzB5kNXQOrpMV_pRBu78Np9ffoPvEML6HrygIGtAcAD_IKuS6AM3dG8pQh4roskwlplzROLO8LTemrtWKYoOIHLZJGvZun&0RQcg1Ab=4HS4LbLoPyR8yp7Eipc6F5r1OvrAdo2BS2tSsiEB0oey1kxpObqdlBIWAr3uhF41sliTHFAWe5J_btNOcHWytB3_FXvq0fKDkshLvue5LV8BUn4CY8wZO0GCZtMWypV93YZ1J0xDTyTJjCsX0AWcP32GsnRZHQrRABQ4p2TgJDKsH50uBpyXwohbFXUhcLlUwoOiONXHmcFkyvrk9G6nndcF8aIOLsGk88MU90R3vkTGt38iTwI35uRJ2hwJxvNkU0kSjTEsTJWQNiOuVo_kS7A
http://wwj.gansu.gov.cn/common/search/0e77c906ca5843e88f17b3f0f3c03a5f?FfNKEgqG=589tgEVoS9FDeaS7W0nDVUpoEAUXepYZeMKaavX7FD6wYStAB1yBpiPb42FM17DO7Tsnc8PHPGdA8T7u.R0E9hKAhdfNxIMFI9tQZebU6TIpwCYtyYwKsCQ0Wop_PWjAdT5DT4gI9TmY6wNSyt.uDxukqeVXDTVNGx1OEX4Nxpswlj0euHokMgeAvzGNk1ghpzM__cqXuFtmmSCMNfkWw9Q0xggBnvAIa0oqRyoOabB142WdUANnZ.JWEhKAJAW2yQzj..hENenYaoLKP4FhOVoKawDZGWuLQAmGgRy2IKK4WckqxUEm0GU059yjr53V_&0RQcg1Ab=4cw1YoNuMXn30ziwkZ_Ggz9WRKRTiHzdm7zl07Ac71Z5N7sigAIrSTQU9G_UZmdsjGof5XUOAm9E_rUZBLOgsa5C.JqEobbhE2zfnn2Kea.0NatauxnsSlBeEm7xxDV_L9kMbewPgpmJbKbIfnsxE3R7K9N0fmiBY5xUe2336zQOGOK7DlFJqYnURT63DkF_JFe748bK5xGap1N52USRa9kDR7UEAwDzqrcT.yO1rdowX2Kproj1PoUwS5pImykM25uNGQ.GgYo2XMuF6kC7b0a
http://wwj.gansu.gov.cn/common/search/0e77c906ca5843e88f17b3f0f3c03a5f?FfNKEgqG=5EWq4HU0YyBQ37D_tt88_brxVY.AfSJQXPSXsRKH3Us3X7hy3qdkZ0mwaGuLQapIhdPyID0QZhZsC7RApttlmh_j3EDWI2abItBR2B7mU3cqFB.nJapf.MiWmJVPoTRFrYMdJKgykFlFZG.TkEnUWH6TIFbs7z5ADOG2dIp0CgyDBktIaJxq8N5nTqC2iAwveQq8QlQl5Rgbb_KU2WSagAnKMhq69vZC714FvWfItBP60AvauBlte6rkuW6jd5hMMj8fsm.px01Q_M2wue0BY478NrDNuPX5KXgXpurjk14h4SSp9cve0RfkhmcdbSkmF&0RQcg1Ab=4nOtVbuLV68cvGCFX6N03fwUUoY2rrOCTcfH1r6.qsPqu1KLpB6pX6NIqQ547pCXHffdk.RTPw.C9WOPegY2FUxFMjf5xp8IhzACThBKhlmM9MBmb08AwG4jgeUnTuT2HLvfNsLZJEMaOO.W72XH.cBXqhyS1vVMY.lL9J_TULS2JDYMC3X9pwQ1rIK38La28XrYtpxOJY5FizJyqdswRUSqpx74AvAYEBkLM39F.OQNuVeLiM1JvLX4HJzv2CF6ouFk6ItE5JIKMEpDM4ljIYA
"""