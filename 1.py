from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.shopify.com/")
driver.maximize_window()

# actionChain = ActionChains(driver)

# driver.find_element_by_link_text("문자")
# driver.find_elements_by_link_text("문자")[0]
# driver.find_element_by_xpath('//*[@id="licenseType"]').send_keys("Licensed Acupuncturist")
# driver.find_element_by_xpath('//*[@id="licenseNumber"]').send_keys("1")
# driver.find_element_by_xpath('//*[@id="wrap"]/main/section/div/article[1]/a[2]').click()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="videojs_html5_api"]')))

# -------------------------------------------------------------------------login

driver.find_element_by_xpath('//*[@id="ShopifyMainNav"]/ul[3]/li[3]/a').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="account_email"]').click()
driver.find_element_by_xpath('//*[@id="account_email"]').send_keys("jinleeyag@gmail.com")
driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div/div/div/div/div[2]/div/form/button').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="account_password"]').click()
driver.find_element_by_xpath('//*[@id="account_password"]').send_keys("March03)#")
driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/ul/button').click()
time.sleep(20)




driver.find_element_by_xpath('//*[@id="AppFrameNav"]/nav/div[2]/ul[1]/li[3]/div[1]/a').click()# Products
time.sleep(3)
driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div[1]/div/div[2]/div[2]/a').click()# Add product
time.sleep(3)


driver.find_element_by_xpath('//*[@id="PolarisTextField17"]').click()# Title
driver.find_element_by_xpath('//*[@id="PolarisTextField17"]').send_keys(ptitle)



#
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="aspnetForm"]/div[3]/div/div/div/div/div/div/div/div/div/div[2]/ul[1]/li[2]/a'))).click()# search
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabAccountManager_tabSearchPanel2_lnk_All"]'))).click()# all
#
#
# wb = Workbook() # new workbook
# ws = wb.active # call a sheet
# ws_y=1
#
# for page in range(2,54):
#     for pi in range(3,23):
#         pi = str(pi).zfill(2)
#         # ptid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dgPatientResults"]/tbody/tr['+str(pi-1)+']/td[2]'))).text# patient id
#         try:
#             print(pi)
#             time.sleep(5)
#             driver.switch_to.window(driver.window_handles[0])
#             pt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dgPatientResults_ctl'+str(pi)+'_ViewRosterMember"]')))# patient select
#             ActionChains(driver).key_down(Keys.CONTROL).click(pt).key_up(Keys.CONTROL).perform()# open in new tab
#             driver.switch_to.window(driver.window_handles[1])# tab switch
#
#             try:
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dgEligibilityResults_ctl02_ViewMember"]'))).click()# eligibility
#
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Referal_Requirment_Panel"]'))).click()# ref
#                 time.sleep(1)
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Covered_Cond_Header_Panel"]'))).click()# dx
#                 time.sleep(1)
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CPS_Info"]'))).click()# mnr
#                 time.sleep(1)
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="feeScheduleHeaderPanel"]'))).click()# fee
#                 time.sleep(1)
#                 # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Claims_Header_Panel"]'))).click()# claim
#
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tblMemberInformation"]')))# basic info
#                 name = driver.find_element_by_xpath('//*[@id="lblMemberName"]').text
#                 ws.cell(column=1, row=ws_y, value=name)
#
#                 grpnum = driver.find_element_by_xpath('//*[@id="lblGroup_no"]').text
#                 ws.cell(column=2, row=ws_y, value=grpnum)
#
#                 id = driver.find_element_by_xpath('//*[@id="lblMem_Id"]').text
#                 ws.cell(column=3, row=ws_y, value=id)
#
#                 ctrnum = driver.find_element_by_xpath('//*[@id="lblContract"]').text
#                 ws.cell(column=4, row=ws_y, value=ctrnum)
#
#                 inspln = driver.find_element_by_xpath('//*[@id="lblHealthPlan"]').text
#                 ws.cell(column=5, row=ws_y, value=inspln)
#
#                 try:
#                     bnftnote = driver.find_element_by_xpath('//*[@id="tblBenefitNotes"]/tbody').text# benefit note
#                     ws.cell(column=6, row=ws_y, value=bnftnote)
#                 except:
#                     ws.cell(column=6, row=ws_y, value="none")
#
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tblBenefits"]/tbody')))# benefit info
#                 benefit = driver.find_element_by_xpath('//*[@id="tblBenefits"]/tbody').text# all benefit
#                 ws.cell(column=7, row=ws_y, value=benefit)
#
#                 try:
#                     benefit1 = driver.find_element_by_xpath('//*[@id="tblBenefits"]/tbody/tr[1]/td[3]').text# copay
#                     ws.cell(column=8, row=ws_y, value=benefit1)
#                 except:
#                     pass
#
#                 try:
#                     benefit2 = driver.find_element_by_xpath('//*[@id="tblBenefits"]/tbody/tr[2]/td[3]').text# year visit
#                     ws.cell(column=9, row=ws_y, value=benefit2)
#                 except:
#                     pass
#
#                 try:
#                     benefit3 = driver.find_element_by_xpath('//*[@id="tblBenefits"]/tbody/tr[3]/td[3]').text# used visit
#                     ws.cell(column=10, row=ws_y, value=benefit3)
#                 except:
#                     pass
#
#                 try:
#                     benefit4 = driver.find_element_by_xpath('//*[@id="tblBenefits"]/tbody/tr[4]/td[3]').text# out of pocket max
#                     ws.cell(column=11, row=ws_y, value=benefit4)
#                 except:
#                     pass
#
#                 try:
#                     benefit5 = driver.find_element_by_xpath('//*[@id="tblBenefits"]/tbody/tr[5]/td[3]').text#
#                     ws.cell(column=12, row=ws_y, value=benefit5)
#                 except:
#                     pass
#
#                 try:
#                     benefit6 = driver.find_element_by_xpath('//*[@id="tblBenefits"]/tbody/tr[6]/td[3]').text#
#                     ws.cell(column=13, row=ws_y, value=benefit6)
#                 except:
#                     pass
#
#                 try:
#                     cmt = driver.find_element_by_xpath('//*[@id="trVisitsused"]/td').text# benefit comment
#                     ws.cell(column=14, row=ws_y, value=cmt)
#                 except:
#                     pass
#
#
#                 try:
#                     ref = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Referral_Requirment_div"]/p[1]'))).text# referral
#                     ws.cell(column=15, row=ws_y, value=ref)
#                 except:
#                     ws.cell(column=15, row=ws_y, value='error')
#
#                 try:
#                     dx = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Covered_Cond_div"]/p[1]'))).text# dx
#                     ws.cell(column=16, row=ws_y, value=dx)
#                 except:
#                     ws.cell(column=16, row=ws_y, value='error')
#
#                 try:
#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CPS_Info_div"]/p[1]')))
#                     mnr = driver.find_element_by_xpath('//*[@id="CPS_Info_div"]').text# mnr
#                     ws.cell(column=17, row=ws_y, value=mnr)
#                 except:
#                     ws.cell(column=17, row=ws_y, value='error')
#
#                 try:
#                     time.sleep(5)
#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lbFeeSchedule"]'))).click()# fee
#                     try:
#                         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnDisplayFeeSchedule"]'))).click()
#                         try:
#                             fee1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbl_1"]/tbody'))).text
#                         except:
#                             fee1 = "none"
#                         try:
#                             fee2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbl_2"]/tbody'))).text
#                         except:
#                             fee2 = "none"
#                         try:
#                             fee3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbl_3"]/tbody'))).text
#                         except:
#                             fee3 = "none"
#                         ws.cell(column=18, row=ws_y, value=fee1+fee2+fee3)
#                     except:
#                         ws.cell(column=18, row=ws_y, value='error')
#                 except:
#                     ws.cell(column=18, row=ws_y, value='error')
#
#             except:
#                 ws.cell(column=1, row=ws_y, value='error')
#
#             wb.save("1.xlsx")
#             driver.close()
#             ws_y += 1
#             print('end')
#         except:
#             ws.cell(column=1, row=ws_y, value='error')
#             print('error')
#             wb.save("1.xlsx")
#             ws_y += 1
#
#         wb.save("1.xlsx")
#
#     driver.switch_to.window(driver.window_handles[0])
#     time.sleep(1)
#     page = str(page)
#     print('page '+page)
#     try:
#         driver.find_element_by_link_text(page).click()
#     except:
#         try:
#             driver.find_elements_by_link_text('...')[1].click()
#         except:
#             driver.find_elements_by_link_text('...')[0].click()
#
#
#
# # test
#
#
#
# # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Referral_Requirment_div"]/h5')))# ref
# # ref = driver.find_element_by_xpath('//*[@id="Referral_Requirment_div"]').text
# # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Covered_Cond_div"]/h5')))# dx
# # dx = driver.find_element_by_xpath('//*[@id="Covered_Cond_div"]/p[1]').text
# # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CPS_Info_div"]/h5[1]')))# mnr
# # mnr = driver.find_element_by_xpath('//*[@id="CPS_Info_div"]').text
# # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="feeScheduleDiv"]/h5')))# fee
# # fee = driver.find_element_by_xpath('//*[@id="feeScheduleDiv"]').text
# # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Claims_Desc_div"]/h5[1]')))# claim
# # clm = driver.find_element_by_xpath('//*[@id="Claims_Desc_div"]').text
# #
# # print('"%s","%s","%s","%s","%s","%s"' % (bas, ref, dx, mnr, fee, clm))
# #
# # driver.close()
# # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dgPatientResults_ctl04_ViewRosterMember"]'))).click()
# #
# #
# # wb = Workbook() # 새 워크북 생성
# # ws = wb.active # 현재 활성화된 sheet 가져옴
# # # ws.title = "jinlee" # sheet 이름 변경
# # # ws.sheet_properties.tabColor = "ff66ff"
# # # ws2 = wb.create_sheet("jinlee2", 2)
# # # ws2 = wb["jinlee2"]
# # # ws2["A1"] = "Test"
# # ws2.cell(column=1, row=2, value=1)
# # # ws3 = wb.copy_worksheet(ws2)
# #
# # ws4 = wb.create_sheet("range")
# # index = 1
# # for y in range(1,11):
# #     for x in range(1,11):
# #         ws4.cell(column=x, row=ws_y, value=index)
# #         index += 1
# #
# #
# # ws5 = wb.create_sheet("apx")
# # ws5.append(["국어", "영어", "수학"])
# # for i in range(1,11):
# #     ws.append([i,randint(1,100),randint(1,100)])
# #
# #
# # print(wb.sheetnames)
# # print(ws2["A1"].value)
# # print(ws2.cell(column=1, row=1).value)
# #
# # wb.save("1.xlsx")
# # wb.close()
#
# # time.sleep(1)
# # time.sleep(1)
# # driver.find_element_by_xpath('//*[@id="wrap"]/main/article/div[2]/iframe').click()
# # time.sleep(1)
# # driver.find_element_by_xpath('//*[@id="wrap"]/main/article/div[2]/iframe').click()
# # time.sleep(1)
# # driver.find_element_by_xpath('//*[@id="wrap"]/main/article/div[2]/iframe').click()
# # time.sleep(1)
# # driver.find_element_by_xpath('//*[@id="videojs_html5_api"]').click()
# #
# # time.sleep(1)
# # elem = driver.find_element_by_xpath('//*[@id="videojs"]')
# #
# # actionChain.context_click(elem).perform()
#
# # try:
# #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]/footer/ul[1]/li[1]/h3')))
# # finally:
# #     None
# #
# #
# # lic = ["1", "2", "3", "4", "5"]
# #
# # for i in lic:
# #     driver.find_element_by_xpath('//*[@id="licenseNumber"]').clear()
# #     driver.find_element_by_xpath('//*[@id="licenseNumber"]').send_keys(i)
# #     driver.find_element_by_xpath('//*[@id="srchSubmit"]').click()
# #     try:
# #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]/footer/ul[1]/li[1]/h3')))
# #     finally:
# #         None
# #     name = driver.find_element_by_xpath('//*[@id="0"]/footer/ul[1]/li[1]/h3').text
# #     num =  driver.find_element_by_xpath('//*[@id="lic0"]').text
# #     print("%s / %s" % (name, num))
