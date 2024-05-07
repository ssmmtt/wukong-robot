# 连接OBS

from obswebsocket import obsws, requests

ws = obsws('localhost', 4455)
ws.connect()

# 发送请求获取所有来源列表
scene = ws.call(requests.GetSceneItemList(sceneName='场景'))
box_id = 0
phone_id = 0

for i in scene.datain['sceneItems']:
    print(i['sceneItemId'])
    print(i['sourceName'])
    print(i['sourceUuid'])
    print('---------------------')
    if i['sourceName'] == '弹窗':
        box_id = i['sceneItemId']
    elif i['sourceName'] == '手机':
        phone_id = i['sceneItemId']

if box_id == 0 or phone_id == 0:
    print('未获取到obs指定的来源')
    exit(1)


def obs_box_open(window_name='box'):
    if window_name == 'box':
        ws.call(requests.SetSceneItemEnabled(sceneName='场景', sceneItemId=box_id, sceneItemEnabled=True))
    elif window_name == 'phone':
        ws.call(requests.SetSceneItemEnabled(sceneName='场景', sceneItemId=phone_id, sceneItemEnabled=True))


def obs_box_close(window_name='box'):
    if window_name == 'box':
        ws.call(requests.SetSceneItemEnabled(sceneName='场景', sceneItemId=box_id, sceneItemEnabled=False))
    elif window_name == 'phone':
        ws.call(requests.SetSceneItemEnabled(sceneName='场景', sceneItemId=phone_id, sceneItemEnabled=False))


if __name__ == '__main__':
    import time

    obs_box_open()
    time.sleep(3)
    obs_box_close()
    time.sleep(3)
    obs_box_open('phone')
    time.sleep(3)
    obs_box_close('phone')
