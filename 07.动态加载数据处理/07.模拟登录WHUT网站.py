import time

from selenium import webdriver
from PIL import Image
import chaojiying


def main():
    browser = webdriver.Chrome('./chromedriver')

    # 打开登录页面
    browser.get('http://218.197.101.24')
    time.sleep(1)

    # 截图
    """
    save_screenshot(fileName) 就是对当前页面进行截图
    """
    browser.save_screenshot('./aa.png')

    # 需要对验证码图片进行裁剪
    # 确定验证码图片的左上角和右下角的坐标（裁剪的区域就确定）
    code_img_ele = browser.find_element_by_xpath('//*[@id="VerifyCode"]')  # 获取验证码图片
    location = code_img_ele.location  # 图片左上角坐标
    size = code_img_ele.size  # 验证码对应的长和宽
    # 左上角右下角坐标， 验证码图片就确定下来了 //*[@id="J-loginImg"]
    rangle = (int(location['x']), int(location['y']),
              int(location['x'] + size['width']), int(location['y'] + size['height']))

    i = Image.open('./aa.png')
    code_img_name = './code.png'
    # 使用crop根据指定区域进行裁剪
    frame = i.crop(rangle)
    frame.save(code_img_name)

    username_input = browser.find_element_by_xpath('//*[@id="txtUserID"]')
    pwd_input = browser.find_element_by_xpath('//*[@id="txtUserPwd"]')
    code_input = browser.find_element_by_xpath('//*[@id="yzm"]')

    username_input.send_keys('账号')
    time.sleep(1)
    pwd_input.send_keys('密码')
    time.sleep(1)
    code_input.send_keys(chaojiying.getCodeText('./code.png', 1902))
    time.sleep(1)

    login_button = browser.find_element_by_xpath('//*[@id="ff"]/table/tbody/tr[5]/td[2]/input[1]')
    login_button.click()

    time.sleep(5)

    browser.quit()


if __name__ == '__main__':
    main()
