# selenium模块的基本使用

## 问题：selenium模块和爬虫之间具有怎样的管理？
- 便捷地获取网站中动态加载的数据
- 便捷地实现模拟登录

## 什么是selenium模块？
- 基于浏览器自动化的一个模块

## selenium使用流程
- 环境安装
    - `pip install selenium`
- 需要下载一个浏览器的驱动程序
    - Chrome
    - [chromedriver下载](https://blog.csdn.net/One_of_them/article/details/82560880)
- 实例化一个浏览器对象
    - `bro = webdriver.Chrome(executable_path='./chromedriver')`
- 编写基于浏览器自动化的操作代码
    - 发起请求：get(url)
    - 标签定位：find系列方法
    - 标签交互：send_keys('xxx')
    - 执行js程序：excute_script('xxx')
    - 前进、后退 forward()/back()
    - 关闭浏览器 quit()
- selenium处理iframe
    - 如果定位的标签存在于iframe标签之中，则需要切换浏览器的标签作用域
        - `browser.switch_to.frame('iframeResult')` iframeResult为iframe标签的ID
    - 执行拖动的动作，依赖于动作链
        - `from selenium.webdriver import ActionChains  # 导入动作链`
        - 实例化action
            - `action = ActionChains(browser)`
        - 点击长按
            - `action.click_and_hold(div)`
        - 执行拖动
            - `action.move_by_offset(17, 0).perform()`
            - perform()表示动作立即执行动作链操作
            - move_by_offset(x, y) x表示水平方向的偏移，y表示竖直方向的偏移