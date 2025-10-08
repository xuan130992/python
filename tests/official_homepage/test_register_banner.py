from pagesPOM.base_page import Base
from pagesPOM.login_page import LoginPage
from pagesPOM.bubblely.Official_homepage.register_component import register_component
from pagesPOM.bubblely.Official_homepage.register_banner import registerbanner_page
from Util.common_functions import CommonFunctions
def test_register_banner_successful(page):
    login_page1 = LoginPage(page)
    register_component1=register_component(page)
    register_banner_page1 = registerbanner_page(page)
    common_functions1 = CommonFunctions(page)
    login_page1.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')
    register_component1.register_component_act("korea")
    register_banner_page1.register_banner_component(common_functions1.feature_title,"0")
    common_functions1.upload_image("(//*[contains(text(),'Upload')])[1]","./resourse/banner_images/png_1300x325.png")




