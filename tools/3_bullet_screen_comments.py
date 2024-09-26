import requests


# 1
# bullet screen comment.
# -- requests.post(url, data, headers)
# -- tutorial: https://www.bilibili.com/video/BV15s4y1L7qV/?spm_id_from=333.880.my_history.page.click&vd_source=a8374ac38c77856369542fc154a1e043

url="https://api.live.bilibili.com/msg/send"

data = {
    "bubble": 0,
    "msg": "都对都对",
    "color": 16777215,
    "mode": 1,
    "room_type": 0,
    "jumpfrom": 71004,
    "reply_mid": 0,
    "reply_attr": 0,
    "replay_dmid": '',
    "statistics": {"appId":100,"platform":5},
    "reply_type": 0,
    "reply_uname":'',
    "fontsize": 125,
    "rnd": 1726995501,
    "roomid": 1704233086,
    "csrf": "8b31fdb960ec1590f09d72f436a9c38b",
    "csrf_token": "8b31fdb960ec1590f09d72f436a9c38b",
}

headers = {
    "cookie":"buvid3=EA696001-1BCB-0F56-08F4-C8BFAD2A2D5809878infoc; b_nut=1708589209; _uuid=1C7BAB110-B386-29C1-88DF-59102BB95BBAB10243infoc; buvid_fp=2ced5cd0984afab05166976d506aa2ac; buvid4=835B46C1-976B-E065-5F4A-468EF695896010781-024022208-b%2BgEsp3ZUr66zu8q0vCo6g%3D%3D; DedeUserID=27573552; DedeUserID__ckMd5=42c75c14f04f4986; CURRENT_FNVAL=4048; rpdid=|(JY)JRkRuYk0J'u~|)l)mk)u; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_HEADER_LIVE_NEW_POP; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=116; LIVE_BUVID=AUTO3817160334963787; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjcwMTYwNzUsImlhdCI6MTcyNjc1NjgxNSwicGx0IjotMX0.hgS2RicvNBQZLn5t6vyh2pL7N4mVoWwtPfFPTiMqhcg; bili_ticket_expires=1727016015; SESSDATA=eaf31b3e%2C1742308889%2C2190a%2A92CjBAzrxqmG0nfTn3V59_g6nyJJ3AhRF6YIN8FV9jpGEWu8hfXOe-PN7JcF4IJwBepNUSVjByaUlpUXhTOWFIV3F5cF9QMVNDT0NsOVVMX2RaRE16Y3dDQU1KMGJEd2lwYVZ3dHlpQmY4dnBBZUJMQkZXamhvUTRxVHRieWN6X3lmWkZjT0xXa19BIIEC; bili_jct=8b31fdb960ec1590f09d72f436a9c38b; sid=8jjsl540; browser_resolution=1512-823; b_lsid=F10ADD42C_19218E65EF6; bp_t_offset_27573552=979926187633541120; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1726995388; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1726995388; HMACCOUNT=2725FBE97BA78289; PVID=4",
    "origin": "https://live.bilibili.com",
    "priority": "u=1, i",
    "referer": "https://live.bilibili.com/1704233086?hotRank=0&session_id=0d506b8fa7a86aa11b6a82242966efdc_0A27099B-B24C-4FA8-B669-86A5A0F1F6FC&launch_id=1000237&live_from=71004",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
response = requests.post(url=url, data=data, headers=headers)

print(response.status_code)
print(response.json())