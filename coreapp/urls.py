from . import views
from django.views.generic import TemplateView
from django.urls import path, re_path
urlpatterns=[
    re_path(r'^$', views.log1, name='login'),
    re_path(r'^home$', views.home, name='home'),
    re_path(r'^pie_chart$', views.pie_chart, name='pie_chart'),

    re_path(r'^$', views.MANmanagerprofile, name='MANmanagerprofile'),
    re_path(r'^MANmanagerprofile1$', views.MANmanagerprofile1, name='MANmanagerprofile1'),
    re_path(r'^MANmanagerprofile$', views.MANmanagerprofile, name='MANmanagerprofile'),
    re_path(r'^MANtask$', views.MANtask, name='MANtask'),
    re_path(r'^MANgivetask$', views.MANgivetask, name='MANgivetask'),
    re_path(r'^MANgivetasktoemployee$', views.MANgivetasktoemployee, name='MANgivetasktoemployee'),
    re_path(r'^MANTaskGivetaskToEmployeeAssign$', views.MANTaskGivetaskToEmployeeAssign,
        name='MANTaskGivetaskToEmployeeAssign'),
    re_path(r'^loadEmployees$', views.loadEmployees, name='loadEmployees'),
    re_path(r'^MANemployees$', views.MANemployees, name='MANemployees'),
    re_path(r'^MANemp$', views.MANemp, name='MANemp'),
    re_path(r'^loadDesignation$', views.loadDesignation, name='loadDesignation'),
    re_path(r'^MANloademployeess$', views.MANloademployeess, name='MANloademployeess'),
    re_path(r'^MANloaddesi$', views.MANloaddesi, name='MANloaddesi'),
    re_path(r'^MANgiveprojects$', views.MANgiveprojects, name='MANgiveprojects'),
    re_path(r'^MANtasksuccess$', views.MANtasksuccess, name='MANtasksuccess'),
    re_path(r'^manperfoDesignation$', views.manperfoDesignation, name='manperfoDesignation'),
    re_path(r'^MANperemp$', views.MANperemp, name='MANperemp'),
    re_path(r'^MANperformance$', views.MANperformance, name='MANperformance'),
    re_path(r'^MANprojects$', views.MANprojects, name='MANprojects'),
    re_path(r'^manprojectsuccess$', views.manprojectsuccess, name='manprojectsuccess'),
    re_path(r'^loadmanprogive$', views.loadmanprogive, name='loadmanprogive'),
    re_path(r'^loadmanprodesi$', views.loadmanprodesi, name='loadmanprodesi'),
    re_path(r'^mangivepro$', views.mangivepro, name='mangivepro'),
    re_path(r'^loadmanproemp$', views.loadmanproemp, name='loadmanproemp'),
    re_path(r'^MANemployees1$', views.MANemployees1, name='MANemployees1'),
    re_path(r'^loadmantaskemp$', views.loadmantaskemp, name='loadmantaskemp'),
    re_path(r'^MANperformance1$', views.MANperformance1, name='MANperformance1'),
    re_path(r'^MANpie_chart$', views.MANpie_chart, name='MANpie_chart'),
    re_path(r'^MANbar_chart$', views.MANbar_chart, name='MANbar_chart'),
    re_path(r'^MANhrpie_chart$', views.MANhrpie_chart, name='MANhrpie_chart'),
    re_path(r'^MANhrbar_chart$', views.MANhrbar_chart, name='MANhrbar_chart'),
    re_path(r'^MANperinsert$', views.MANperinsert, name='MANperinsert'),
    re_path(r'^MANmyprobar_chart$', views.MANmyprobar_chart, name='MANmyprobar_chart'),
    re_path(r'^MANmypropie_chart$', views.MANmypropie_chart, name='MANmypropie_chart'),

    re_path(r'^traineeloadDesignation$', views.traineeloadDesignation, name='traineeloadDesignation'),
    re_path(r'^MANtraineebutton$', views.MANtraineebutton, name='MANtraineebutton'),
    re_path(r'^MANtrainees$', views.MANtrainees, name='MANtrainees'),
    re_path(r'^MANtrainees1$', views.MANtrainees1, name='MANtrainees1'),
    re_path(r'^MANattendance$', views.MANattendance, name='MANattendance'),
    re_path(r'^MANemployeeAttendance$', views.MANemployeeAttendance, name='MANemployeeAttendance'),
    re_path(r'^loadmanemployeeatten$', views.loadmanemployeeatten, name='loadmanemployeeatten'),
    re_path(r'^employattendancebtn$', views.employattendancebtn, name='employattendancebtn'),
    re_path(r'^MANHRAttendance$', views.MANHRAttendance, name='MANHRAttendance'),
    re_path(r'^MANLeaverequests$', views.MANLeaverequests, name='MANLeaverequests'),
    re_path(r'^MANLeaverequests1$', views.MANLeaverequests1, name='MANLeaverequests1'),
    re_path(r'^accptORreject$', views.accptORreject, name='accptORreject'),

    re_path(r'^MANmarketing$', views.MANmarketing, name='MANmarketing'),
    re_path(r'^Massignwork$', views.Massignwork, name='Massignwork'),
    re_path(r'^MANmarkassignwrk$', views.MANmarkassignwrk, name='MANmarkassignwrk'),
    re_path(r'^MANmarketingassignwrksuccess$', views.MANmarketingassignwrksuccess, name='MANmarketingassignwrksuccess'),
    re_path(r'^MANmarketingMyWork$', views.MANmarketingMyWork, name='MANmarketingMyWork'),
    re_path(r'^MANmarkserviceslist$', views.MANmarkserviceslist, name='MANmarkserviceslist'),
    re_path(r'^MANmarkProductlist$', views.MANmarkProductlist, name='MANmarkProductlist'),
    re_path(r'^MANmarkRecriutmentlist$', views.MANmarkRecriutmentlist, name='MANmarkRecriutmentlist'),
    re_path(r'^MANmarkProductDetails$', views.MANmarkProductDetails, name='MANmarkProductDetails'),
    re_path(r'^MANmarkServiceDetails$', views.MANmarkServiceDetails, name='MANmarkServiceDetails'),
    re_path(r'^MANmarkRecruitmentDetails$', views.MANmarkRecruitmentDetails, name='MANmarkRecruitmentDetails'),
    re_path(r'^MANmarkProductDetailsShare$', views.MANmarkProductDetailsShare, name='MANmarkProductDetailsShare'),
    re_path(r'^MANmarkServiceDetailsShare$', views.MANmarkServiceDetailsShare, name='MANmarkServiceDetailsShare'),
    re_path(r'^MANmarkRecruitmentDetailsShare$', views.MANmarkRecruitmentDetailsShare,
        name='MANmarkRecruitmentDetailsShare'),
    re_path(r'^MANreportedissues$', views.MANreportedissues, name='MANreportedissues'),
    re_path(r'^MANreportedissues1$', views.MANreportedissues1, name='MANreportedissues1'),
    re_path(r'^MANreportedissues2$', views.MANreportedissues2, name='MANreportedissues2'),
    re_path(r'^Mhrattendance$', views.Mhrattendance, name='Mhrattendance'),
    re_path(r'^MANmanageHR$', views.MANmanageHR, name='MANmanageHR'),
    re_path(r'^givetasktoHR$', views.givetasktoHR, name='givetasktoHR'),
    re_path(r'^MANmanageHRgivetask$', views.MANmanageHRgivetask, name='MANmanageHRgivetask'),
    re_path(r'^MANassignedtaskSubmitted$', views.MANassignedtaskSubmitted, name='MANassignedtaskSubmitted'),
    re_path(r'^MANassignedtask1$', views.MANassignedtask1, name='MANassignedtask1'),
    re_path(r'^MANassignedtask$', views.MANassignedtask, name='MANassignedtask'),
    re_path(r'^MANassigntasklistclick$', views.MANassigntasklistclick, name='MANassigntasklistclick'),
    re_path(r'^MANassignedpro$', views.MANassignedpro, name='MANassignedpro'),
    re_path(r'^MANassignedprojects1$', views.MANassignedprojects1, name='MANassignedprojects1'),
    re_path(r'^MANassignedprojectsSubmitted$', views.MANassignedprojectsSubmitted, name='MANassignedprojectsSubmitted'),
    re_path(r'^MANassignedproject$', views.MANassignedproject, name='MANassignedproject'),
    re_path(r'^MANmytasks$', views.MANmytasks, name='MANmytasks'),
    re_path(r'^MANtask1$', views.MANtask1, name='MANtask1'),
    re_path(r'^MANmydupdate$', views.MANmydupdate, name='MANmydupdate'),
    re_path(r'^MANmytaskupdate$', views.MANmytaskupdate, name='MANmytaskupdate'),
    re_path(r'^MANmanageHRsharedtask$', views.MANmanageHRsharedtask, name='MANmanageHRsharedtask'),
    re_path(r'^MANmanagehrassigned$', views.MANmanagehrassigned, name='MANmanagehrassigned'),

    re_path(r'^MANManageHrPerformance$', views.MANManageHrPerformance, name='MANManageHrPerformance'),
    re_path(r'^MANManageHrPerformanceUpdate$', views.MANManageHrPerformanceUpdate, name='MANManageHrPerformanceUpdate'),

    re_path(r'^RemindAction$', views.RemindAction, name='RemindAction'),
    re_path(r'^GiveTaskRemind$', views.GiveTaskRemind, name='GiveTaskRemind'),
    re_path(r'^MANproductmarketingshare$', views.MANproductmarketingshare, name='MANproductmarketingshare'),
    re_path(r'^MANServicemarketingshare$', views.MANServicemarketingshare, name='MANServicemarketingshare'),
    re_path(r'^MANrecruitmarketingshare$', views.MANrecruitmarketingshare, name='MANrecruitmarketingshare'),

    re_path(r'^MANmarketingSharedTask$', views.MANmarketingSharedTask, name='MANmarketingSharedTask'),
    re_path(r'^MANmarketingSharedTaskSub$', views.MANmarketingSharedTaskSub, name='MANmarketingSharedTaskSub'),
    re_path(r'^MANattendncemy$', views.MANattendncemy, name='MANattendncemy'),
    re_path(r'^MANmyattendance$', views.MANmyattendance, name='MANmyattendance'),
    re_path(r'^MANprojectextensionrequest1$', views.MANprojectextensionrequest1, name='MANprojectextensionrequest1'),
    re_path(r'^MANprojectextensionrequest$', views.MANprojectextensionrequest, name='MANprojectextensionrequest'),
    re_path(r'^extndaccptORreject$', views.extndaccptORreject, name='extndaccptORreject'),

    re_path(r'^MANemployeetraineeflowchart$', views.MANemployeetraineeflowchart, name='MANemployeetraineeflowchart'),
    re_path(r'^MANviewdatainsharedtask2$', views.MANviewdatainsharedtask2, name='MANviewdatainsharedtask2'),
    re_path(r'^MANmarketingDirectMarketer$', views.MANmarketingDirectMarketer, name='MANmarketingDirectMarketer'),
    re_path(r'^MANmarketingDirectMarketerfn$', views.MANmarketingDirectMarketerfn, name='MANmarketingDirectMarketerfn'),
    re_path(r'^MANpayments33$', views.MANpayments33, name='MANpayments33'),
    re_path(r'^MANPayments$', views.MANPayments, name='MANPayments'),
    re_path(r'^MANPaymentsViewDetailButton$', views.MANPaymentsViewDetailButton, name='MANPaymentsViewDetailButton'),

    re_path(r'^MANManageHrPerformance1$', views.MANManageHrPerformance1, name='MANManageHrPerformance1'),

    re_path(r'^MANmyproject$', views.MANmyproject, name='MANmyproject'),
    re_path(r'^MANmyprojectsubtask$', views.MANmyprojectsubtask, name='MANmyprojectsubtask'),
    re_path(r'^MANmyprojectsubtaskAdd$', views.MANmyprojectsubtaskAdd, name='MANmyprojectsubtaskAdd'),
    re_path(r'^MANmyprojectSubtaskAddfun$', views.MANmyprojectSubtaskAddfun, name='MANmyprojectSubtaskAddfun'),
    re_path(r'^MANDropdownemp$', views.MANDropdownemp, name='MANDropdownemp'),
    re_path(r'^MANMyprojectsubtaskProjectstatus$', views.MANMyprojectsubtaskProjectstatus, name='MANMyprojectsubtaskProjectstatus'),
    re_path(r'^MANMyprojecttaskextensionstatus$', views.MANMyprojecttaskextensionstatus, name='MANMyprojecttaskextensionstatus'),



    #=============================VARNA
    re_path(r'^pie_chart$', views.pie_chart, name='pie_chart'),
    re_path(r'^bar_chart$', views.bar_chart, name='bar_chart'),
    re_path(r'^hrmypropie_chart$', views.hrmypropie_chart, name='hrmypropie_chart'),
    re_path(r'^acnmypropie_chart$', views.acnmypropie_chart, name='acnmypropie_chart'),
    # ===========================HR====================================
    re_path(r'^hr$', views.hr, name='hr'),
    re_path(r'^hr1$', views.hr1, name='hr1'),
    re_path(r'^hrmydupdate$', views.hrmydupdate, name='hrmydupdate'),
    re_path(r'^hrtasks$', views.hrtasks, name='hrtasks'),
    re_path(r'^hrgiveprojects$', views.hrgiveprojects, name='hrgiveprojects'),
    re_path(r'^hrtasks1$', views.hrtasks1, name='hrtasks1'),
    re_path(r'^hrtasksuccess$', views.hrtasksuccess, name='hrtasksuccess'),
    re_path(r'^hrmytasks$', views.hrmytasks, name='hrmytasks'),
    re_path(r'^hrassignedtasks$', views.hrassignedtasks, name='hrassignedtasks'),
    re_path(r'^hremployeess$', views.hremployeess, name='hremployeess'),
    re_path(r'^loadhremployeess$', views.loadhremployeess, name='loadhremployeess'),
    re_path(r'^hrreportissues$', views.hrreportissues, name='hrreportissues'),
    re_path(r'^hrreport1$', views.hrreport1, name='hrreport1'),
    re_path(r'^hrreportsuccess$', views.hrreportsuccess, name='hrreportsuccess'),
    re_path(r'^hremp$', views.hremp, name='hremp'),
    re_path(r'^hrempdesi$', views.hrempdesi, name='hrempdesi'),
    re_path(r'^hremployees1$', views.hremployees1, name='hremployees1'),
    re_path(r'^loadhrdesi$', views.loadhrdesi, name='loadhrdesi'),
    re_path(r'^hrprojects$', views.hrprojects, name='hrprojects'),
    re_path(r'^hrprojectsuccess$', views.hrprojectsuccess, name='hrprojectsuccess'),
    re_path(r'^loadhrprogive$', views.loadhrprogive, name='loadhrprogive'),
    re_path(r'^loadhrprodesi$', views.loadhrprodesi, name='loadhrprodesi'),
    re_path(r'^loadhrproemp$', views.loadhrproemp, name='loadhrproemp'),
    re_path(r'^hrgivepro$', views.hrgivepro, name='hrgivepro'),
    re_path(r'^hrperformance$', views.hrperformance, name='hrperformance'),
    re_path(r'^hrperformance1$', views.hrperformance1, name='hrperformance1'),
    re_path(r'^hrperdesi$', views.hrperdesi, name='hrperdesi'),
    re_path(r'^hrper$', views.hrper, name='hrper'),
    re_path(r'^hrtrainees1$', views.hrtrainees1, name='hrtrainees1'),
    re_path(r'^hrviewtrainee$', views.hrviewtrainee, name='hrviewtrainee'),
    re_path(r'^hrtraineedesi$', views.hrtraineedesi, name='hrtraineedesi'),
    re_path(r'^hrtrainee$', views.hrtrainee, name='hrtrainee'),
    re_path(r'^hrtrainees2$', views.hrtrainees2, name='hrtrainees2'),
    re_path(r'^hrattendance$', views.hrattendance, name='hrattendance'),
    re_path(r'^hrputattendance$', views.hrputattendance, name='hrputattendance'),
    re_path(r'^hrattend$', views.hrattend, name='hrattend'),
    re_path(r'^hrreportedissue1$', views.hrreportedissue1, name='hrreportedissue1'),
    re_path(r'^hrreportedissue2$', views.hrreportedissue2, name='hrreportedissue2'),
    re_path(r'^hrreportedupdate$', views.hrreportedupdate, name='hrreportedupdate'),
    re_path(r'^hrattendance2$', views.hrattendance2, name='hrattendance2'),
    re_path(r'^hrattendance1$', views.hrattendance1, name='hrattendance1'),
    re_path(r'^hrattendance3$', views.hrattendance3, name='hrattendance3'),
    re_path(r'^hrreqleaves$', views.hrreqleaves, name='hrreqleaves'),
    re_path(r'^empattend$', views.empattend, name='empattend'),
    re_path(r'^hrassigned1$', views.hrassigned1, name='hrassigned1'),
    re_path(r'^hrattendance4$', views.hrattendance4, name='hrattendance4'),
    re_path(r'^hrattendncemy$', views.hrattendncemy, name='hrattendncemy'),
    re_path(r'^hrassignedprojects$', views.hrassignedprojects, name='hrassignedprojects'),
    re_path(r'^hrassignedpro$', views.hrassignedpro, name='hrassignedpro'),
    re_path(r'^hrGiveTaskRemind$', views.hrGiveTaskRemind, name='hrGiveTaskRemind'),
    re_path(r'^hrviewsyllabus$', views.hrviewsyllabus, name='hrviewsyllabus'),
    re_path(r'^hrsyllabusdesi$', views.hrsyllabusdesi, name='hrsyllabusdesi'),
    re_path(r'^hrsyllabus$', views.hrsyllabus, name='hrsyllabus'),
    re_path(r'^hrattendance5$', views.hrattendance5, name='hrattendance5'),
    re_path(r'^hremployeedesi$', views.hremployeedesi, name='hremployeedesi'),
    re_path(r'^hremployeeattend$', views.hremployeeattend, name='hremployeeattend'),
    re_path(r'^hrtrainees$', views.hrtrainees, name='hrtrainees'),
    re_path(r'^hremployeeflowchart$', views.hremployeeflowchart, name='hremployeeflowchart'),
    re_path(r'^hrmarketing1$', views.hrmarketing1, name='hrmarketing1'),
    re_path(r'^hrPayments1$', views.hrPayments1, name='hrPayments1'),
    re_path(r'^hrPaymentsViewDetailButton$', views.hrPaymentsViewDetailButton, name='hrPaymentsViewDetailButton'),
    re_path(r'^hrpayments33$', views.hrpayments33, name='hrpayments33'),
    re_path(r'^hrsharedtask1$', views.hrsharedtask1, name='hrsharedtask1'),
    re_path(r'^hrsharedtasks2$', views.hrsharedtasks2, name='hrsharedtasks2'),
    re_path(r'^hrsharedtasks$', views.hrsharedtasks, name='hrsharedtasks'),
    re_path(r'^hrviewdeatails$', views.hrviewdeatails, name='hrviewdeatails'),
    re_path(r'^hrperformance2$', views.hrperformance2, name='hrperformance2'),
    re_path(r'^hrmydupdate$', views.hrmydupdate, name='hrmydupdate'),
    re_path(r'^hrmytasks$', views.hrmytasks, name='hrmytasks'),
    re_path(r'^hrmarketingSharedTaskSub$', views.hrmarketingSharedTaskSub, name='hrmarketingSharedTaskSub'),
    re_path(r'^hrperinsert$', views.hrperinsert, name='hrperinsert'),
    re_path(r'^hrputattendancesearch$', views.hrputattendancesearch, name='hrputattendancesearch'),
    re_path(r'^loadhrtaskemp$', views.loadhrtaskemp, name='loadhrtaskemp'),
    re_path(r'^HRMANmyproject$', views.HRMANmyproject, name='HRMANmyproject'),
    re_path(r'^HRMANmyprojectsubtask$', views.HRMANmyprojectsubtask, name='HRMANmyprojectsubtask'),


    # ==================================accounts====================
    re_path(r'^accounts$', views.accounts, name='accounts'),
    re_path(r'^accounts1$', views.accounts1, name='accounts1'),
    re_path(r'^acntemp$', views.acntemp, name='acntemp'),
    re_path(r'^acntempdesi$', views.acntempdesi, name='acntempdesi'),
    re_path(r'^acntemp1$', views.acntemp1, name='acntemp1'),
    re_path(r'^accountemp$', views.accountemp, name='accountemp'),
    re_path(r'^acntemp2$', views.acntemp2, name='acntemp2'),
    re_path(r'^acntexpenses$', views.acntexpenses, name='acntexpenses'),
    re_path(r'^acntnewt$', views.acntnewt, name='acntnewt'),
    re_path(r'^acntviewreceipts$', views.acntviewreceipts, name='acntviewreceipts'),
    re_path(r'^acntreceipts$', views.acntreceipts, name='acntreceipts'),
    re_path(r'^acntempupdate$', views.acntempupdate, name='acntempupdate'),
    re_path(r'^acntpayslips$', views.acntpayslips, name='acntpayslips'),
    re_path(r'^acntnewtsave$', views.acntnewtsave, name='acntnewtsave'),
    re_path(r'^acntexpviewedit$', views.acntexpviewedit, name='acntexpviewedit'),
    re_path(r'^acntexpvieweditupdate$', views.acntexpvieweditupdate, name='acntexpvieweditupdate'),
    re_path(r'^acntdefine$', views.acntdefine, name='acntdefine'),
    re_path(r'^acntpay$', views.acntpay, name='acntpay'),
    re_path(r'^acntpay1$', views.acntpay1, name='acntpay1'),
    re_path(r'^acntsendpay$', views.acntsendpay, name='acntsendpay'),
    re_path(r'^acntattend$', views.acntattend, name='acntattend'),
    re_path(r'^acntsendinsert$', views.acntsendinsert, name='acntsendinsert'),
    re_path(r'^acntviewattend$', views.acntviewattend, name='acntviewattend'),
    re_path(r'^acntview1$', views.acntview1, name='acntview1'),
    re_path(r'^acntremain$', views.acntremain, name='acntremain'),
    re_path(r'^acntrdecline$', views.acntrdecline, name='acntrdecline'),
    re_path(r'^acntpayhis$', views.acntpayhis, name='acntpayhis'),
    re_path(r'^acntpayinsert$', views.acntpayinsert, name='acntpayinsert'),
    re_path(r'^acntprint$', views.acntprint, name='acntprint'),
    re_path(r'^acntGeneratePdf$', views.acntGeneratePdf.as_view(), name='acntGeneratePdf'),

#---------------------tl-------------------------------
    re_path(r'^tl$', views.tl, name='tl'),
    re_path(r'^tlmypropie_chart$', views.tlmypropie_chart, name='tlmypropie_chart'),
    re_path(r'^tl1$', views.tl1, name='tl1'),
    re_path(r'^tlattendance2$', views.tlattendance2, name='tlattendance2'),
    re_path(r'^tlattendance3$', views.tlattendance3, name='tlattendance3'),
    re_path(r'^tlattendance1$', views.tlattendance1, name='tlattendance1'),
    re_path(r'^tlreqleaves$', views.tlreqleaves, name='tlreqleaves'),
    re_path(r'^tlPayments1$', views.tlPayments1, name='tlPayments1'),
    re_path(r'^tlPaymentsViewDetailButton$', views.tlPaymentsViewDetailButton, name='tlPaymentsViewDetailButton'),
    re_path(r'^tlpayments33$', views.tlpayments33, name='tlpayments33'),
    re_path(r'^tlreportissues$', views.tlreportissues, name='tlreportissues'),
    re_path(r'^tlreportedissue1$', views.tlreportedissue1, name='tlreportedissue1'),
    re_path(r'^tlreportedissue2$', views.tlreportedissue2, name='tlreportedissue2'),
    re_path(r'^tlreport1$', views.tlreport1, name='tlreport1'),
    re_path(r'^tlreportsuccess$', views.tlreportsuccess, name='tlreportsuccess'),
    re_path(r'^tlemployeess$', views.tlemployeess, name='tlemployeess'),
    re_path(r'^tlattendncemy$', views.tlattendncemy, name='tlattendncemy'),
    re_path(r'^tlperformance$', views.tlperformance, name='tlperformance'),
    re_path(r'^tlprojects2$', views.tlprojects2, name='tlprojects2'),
    re_path(r'^tlprojects3$', views.tlprojects3, name='tlprojects3'),
    re_path(r'^tlprojects2assign$', views.tlprojects2assign, name='tlprojects2assign'),
    re_path(r'^tlprojects2extend$', views.tlprojects2extend, name='tlprojects2extend'),
    re_path(r'^tlprojects2success$', views.tlprojects2success, name='tlprojects2success'),
    re_path(r'^tlproject2add$', views.tlproject2add, name='tlproject2add'),
    re_path(r'^tltrviewproject2$', views.tltrviewproject2, name='tltrviewproject2'),
    re_path(r'^tlprojects$', views.tlprojects, name='tlprojects'),
    re_path(r'^tltask2$', views.tltask2, name='tltask2'),
    re_path(r'^tltask2add$', views.tltask2add, name='tltask2add'),
    re_path(r'^tltasks$', views.tltasks, name='tltasks'),
    re_path(r'^tlviewtrainee$', views.tlviewtrainee, name='tlviewtrainee'),
    re_path(r'^tlviewtrainee1$', views.tlviewtrainee1, name='tlviewtrainee1'),
    re_path(r'^tluploadtopics$', views.tluploadtopics, name='tluploadtopics'),
    re_path(r'^tluploadtopicsadd$', views.tluploadtopicsadd, name='tluploadtopicsadd'),
    re_path(r'^tlweeklytasks$', views.tlweeklytasks, name='tlweeklytasks'),
    re_path(r'^tlgivetasks$', views.tlgivetasks, name='tlgivetasks'),
    re_path(r'^tlgivetasksadd$', views.tlgivetasksadd, name='tlgivetasksadd'),
    re_path(r'^tlloadhrprodesi$', views.tlloadhrprodesi, name='tlloadhrprodesi'),
    re_path(r'^tlloadhrprogive$', views.tlloadhrprogive, name='tlloadhrprogive'),
    re_path(r'^tlloadhrproemp$', views.tlloadhrproemp, name='tlloadhrproemp'),
    re_path(r'^tlhrprojectsuccess$', views.tlhrprojectsuccess, name='tlhrprojectsuccess'),
    re_path(r'^tltaskgiven$', views.tltaskgiven, name='tltaskgiven'),
    re_path(r'^tltrtask2$', views.tltrtask2, name='tltrtask2'),
    re_path(r'^tltasknotsubmit$', views.tltasknotsubmit, name='tltasknotsubmit'),
    re_path(r'^tltasksubmit$', views.tltasksubmit, name='tltasksubmit'),
    re_path(r'^tltasksubmit2$', views.tltasksubmit2, name='tltasksubmit2'),
    re_path(r'^tlgiveprojects$', views.tlgiveprojects, name='tlgiveprojects'),
    re_path(r'^tlviewprojects$', views.tlviewprojects, name='tlviewprojects'),
    re_path(r'^tlproextend$', views.tlproextend, name='tlproextend'),
    re_path(r'^tlprojects2extendadd$', views.tlprojects2extendadd, name='tlprojects2extendadd'),


    re_path(r'^tlprosubmit$', views.tlprosubmit, name='tlprosubmit'),
    re_path(r'^tlviewprosubmit$', views.tlviewprosubmit, name='tlviewprosubmit'),
    re_path(r'^tlattendance$', views.tlattendance, name='tlattendance'),
    re_path(r'^tlattend$', views.tlattend, name='tlattend'),
    re_path(r'^tlempattend$', views.tlempattend, name='tlempattend'),
    re_path(r'^tlputattendancesearch$', views.tlputattendancesearch, name='tlputattendancesearch'),
    re_path(r'^tlemployeedesi$', views.tlemployeedesi, name='tlemployeedesi'),
    re_path(r'^tlviewattendance$', views.tlviewattendance, name='tlviewattendance'),
    re_path(r'^tlviewattendance1$', views.tlviewattendance1, name='tlviewattendance1'),
    re_path(r'^tltrperformance$', views.tltrperformance, name='tltrperformance'),
    re_path(r'^tltrper$', views.tltrper, name='tltrper'),
    re_path(r'^tltrperformancesearch$', views.tltrperformancesearch, name='tltrperformancesearch'),
    re_path(r'^tltrrperinsert$', views.tltrrperinsert, name='tltrrperinsert'),
    re_path(r'^TLMANmyprojectsubtask$', views.TLMANmyprojectsubtask, name='TLMANmyprojectsubtask'),
    re_path(r'^TLMANMyprojectsubtaskProjectstatus$', views.TLMANMyprojectsubtaskProjectstatus, name='TLMANMyprojectsubtaskProjectstatus'),
    re_path(r'^tlsplitpro$', views.tlsplitpro, name='tlsplitpro'),

    re_path(r'^TLProjectTasks$', views.TLProjectTasks, name='TLProjectTasks'),
    re_path(r'^TLprojectsubtasksAddReport$', views.TLprojectsubtasksAddReport, name='TLprojectsubtasksAddReport'),
    re_path(r'^TLMyprojectsubtaskProjectstatus$', views.TLMyprojectsubtaskProjectstatus, name='TLMyprojectsubtaskProjectstatus'),
    re_path(r'^TLprojectsubtaskextensionrqst$', views.TLprojectsubtaskextensionrqst, name='TLprojectsubtaskextensionrqst'),
    re_path(r'^TLProjectTaskSubtask$', views.TLProjectTaskSubtask, name='TLProjectTaskSubtask'),
    re_path(r'^TLDropdownemp$', views.TLDropdownemp, name='TLDropdownemp'),
    re_path(r'^TLmyprojectSubtaskAddfun$', views.TLmyprojectSubtaskAddfun, name='TLmyprojectSubtaskAddfun'),
    re_path(r'^TLmyprojectsubtaskAdd$', views.TLmyprojectsubtaskAdd, name='TLmyprojectsubtaskAdd'),
    re_path(r'^Tlsplitprojectsubtaskextensionstatus$', views.Tlsplitprojectsubtaskextensionstatus, name='Tlsplitprojectsubtaskextensionstatus'),
    re_path(r'^TLMyprojectsubtaskProjectstatus$', views.TLMyprojectsubtaskProjectstatus, name='TLMyprojectsubtaskProjectstatus'),

    re_path(r'^TLloadmantaskemp$', views.TLloadmantaskemp, name='TLloadmantaskemp'),
    re_path(r'^TLDropdownemp$', views.TLDropdownemp, name='TLDropdownemp'),
    re_path(r'^TLloaddesi$', views.TLloaddesi, name='TLloaddesi'),

    #=====================================developer============
    re_path(r'^dr$', views.dr, name='dr'),
    re_path(r'^drmypropie_chart$', views.drmypropie_chart, name='drmypropie_chart'),
    re_path(r'^dr1$', views.dr1, name='dr1'),
    re_path(r'^drtopics$', views.drtopics, name='drtopics'),
    re_path(r'^drtoptcs2$', views.drtoptcs2, name='drtoptcs2'),
    re_path(r'^drtopic3add$', views.drtopic3add, name='drtopic3add'),
    re_path(r'^drmanagerattendanceadd$', views.drmanagerattendanceadd, name='drmanagerattendanceadd'),


    re_path(r'^drreviewsuccess$', views.drreviewsuccess, name='drreviewsuccess'),
    re_path(r'^drweeklytask$', views.drweeklytask, name='drweeklytask'),
    re_path(r'^drweeklytask2$', views.drweeklytask2, name='drweeklytask2'),
    re_path(r'^drweeklytask2add$', views.drweeklytask2add, name='drweeklytask2add'),


    re_path(r'^drtasksuccess$', views.drtasksuccess, name='drtasksuccess'),
    re_path(r'^drapplyleave$', views.drapplyleave, name='drapplyleave'),
    re_path(r'^drleavereq$', views.drleavereq, name='drleavereq'),
    re_path(r'^drapplyleave2$', views.drapplyleave2, name='drapplyleave2'),

    re_path(r'^drapplyleave3$', views.drapplyleave3, name='drapplyleave3'),


    re_path(r'^drreportissues$', views.drreportissues, name='drreportissues'),
    re_path(r'^drreportedissue1$', views.drreportedissue1, name='drreportedissue1'),
    re_path(r'^drreportedissue2$', views.drreportedissue2, name='drreportedissue2'),
    re_path(r'^drreport1$', views.drreport1, name='drreport1'),
    re_path(r'^drreportsuccess$', views.drreportsuccess, name='drreportsuccess'),
    re_path(r'^drprojects$', views.drprojects, name='drprojects'),
    re_path(r'^drprojects2$', views.drprojects2, name='drprojects2'),
    re_path(r'^drproject2add$', views.drproject2add, name='drproject2add'),

    re_path(r'^d$', views.d, name='d'),
    re_path(r'^d1$', views.d1, name='d1'),
    re_path(r'^drpaymentnotifications2add$', views.drpaymentnotifications2add, name='drpaymentnotifications2add'),


    re_path(r'^drprojects2extend$', views.drprojects2extend, name='drprojects2extend'),
    re_path(r'^drprojects2extendadd$', views.drprojects2extendadd, name='drprojects2extendadd'),


    re_path(r'^drprojrct2extendsuccess$', views.drprojrct2extendsuccess, name='drprojrct2extendsuccess'),
    re_path(r'^drprojects3$', views.drprojects3, name='drprojects3'),
    re_path(r'^drattendance$', views.drattendance, name='drattendance'),
    re_path(r'^drattendncemy$', views.drattendncemy, name='drattendncemy'),


    re_path(r'^drpayments$', views.drpayments, name='drpayments'),
    re_path(r'^drpaymenthistory$', views.drpaymenthistory, name='drpaymenthistory'),
    re_path(r'^drpaymentnotifications$', views.drpaymentnotifications, name='drpaymentnotifications'),
    re_path(r'^drpaymentnotifications2$', views.drpaymentnotifications2, name='drpaymentnotifications2'),


    re_path(r'^drsalaryslip$', views.drsalaryslip, name='drsalaryslip'),
    re_path(r'^drPaymentsViewDetailButton$', views.drPaymentsViewDetailButton, name='drPaymentsViewDetailButton'),
    re_path(r'^drpayments33$', views.drpayments33, name='drpayments33'),

    re_path(r'^DRprojectsubtasks$', views.DRprojectsubtasks, name='DRprojectsubtasks'),
    re_path(r'^DRprojectsubtasksAddStatus$', views.DRprojectsubtasksAddStatus, name='DRprojectsubtasksAddStatus'),
    re_path(r'^DRprojectsubtasksAddReport$', views.DRprojectsubtasksAddReport, name='DRprojectsubtasksAddReport'),
    re_path(r'^DRprojectsubtaskextensionrqst$', views.DRprojectsubtaskextensionrqst, name='DRprojectsubtaskextensionrqst'),

    #-------------------------TS------------------------------
    
    re_path(r'^ts$', views.ts, name='ts'),
    re_path(r'^tsproject$', views.tsproject, name='tsproject'),
    re_path(r'^tsproject2$', views.tsproject2, name='tsproject2'),
    re_path(r'^tsproject2add$', views.tsproject2add, name='tsproject2add'),
    re_path(r'^tstask$', views.tstask, name='tstask'),
    re_path(r'^tstask2$', views.tstask2, name='tstask2'),
    re_path(r'^tstask2add$', views.tstask2add, name='tstask2add'),
    re_path(r'^TSMANmyprojectsubtask$', views.TSMANmyprojectsubtask, name='TSMANmyprojectsubtask'),
    re_path(r'^TSprojectsubtasksAddReport$', views.TSprojectsubtasksAddReport, name='TSprojectsubtasksAddReport'),

    #---------------------------------admin-------------------------
    
    re_path(r'^adminmyprofile$', views.adminmyprofile, name='adminmyprofile'),
    re_path(r'^adminbranch1$', views.adminbranch1, name='adminbranch1'),
    re_path(r'^adminaddbranch1$', views.adminaddbranch1, name='adminaddbranch1'),
    re_path(r'^adminbranchadded$', views.adminbranchadded, name='adminbranchadded'),
    re_path(r'^admininternshipregistration1$', views.admininternshipregistration1, name='admininternshipregistration1'),
    re_path(r'^admininternshipregistration2$', views.admininternshipregistration2, name='admininternshipregistration2'),
    re_path(r'^admininsertcollege$', views.admininsertcollege, name='admininsertcollege'),
    re_path(r'^admindetailsadded1$', views.admindetailsadded1, name='admindetailsadded1'),
    re_path(r'^admindetailsadded$', views.admindetailsadded, name='admindetailsadded'),
    re_path(r'^adminmarketingadm1$', views.adminmarketingadm1, name='adminmarketingadm1'),
#    re_path(r'^adminpromarket1$', views.adminpromarket1, name='adminpromarket1'),
    re_path(r'^admininternshipregistrationdetails$', views.admininternshipregistrationdetails, name='admininternshipregistrationdetails'),

    re_path(r'^editinternship/(?P<id>\d+)$', views.editinternship, name='editinternship'),
    re_path(r'^editinternship/updatinternship/(?P<id>\d+)$', views.updatinternship, name='updatinternship'),
    re_path(r'^deleteinternship/(?P<id>\d+)$', views.deleteinternship, name='deleteinternship'),

    re_path(r'^admininternshipview/(?P<id>\d+)$', views.admininternshipview, name='admininternshipview'),
    re_path(r'^admininternshipview/updateadmininternshipview/(?P<id>\d+)$', views.updateadmininternshipview, name='updateadmininternshipview'),

    re_path(r'^adminregistration$', views.adminregistration, name='adminregistration'),
#    re_path(r'^adminviewbranch1$', views.adminviewbranch1, name='adminviewbranch1'),
    re_path(r'^adminviewbranch2$', views.adminviewbranch2, name='adminviewbranch2'),

    re_path(r'^promarketadd$', views.promarketadd, name='promarketadd'),
#    re_path(r'^serviceadmin$', views.serviceadmin, name='serviceadmin'),
    re_path(r'^serviceadd$', views.serviceadd, name='serviceadd'),
#    re_path(r'^recrutementadmin$', views.recrutementadmin, name='recrutementadmin'),
    re_path(r'^recrutementadd$', views.recrutementadd, name='recrutementadd'),
    re_path(r'^marketingassignedadmin$', views.marketingassignedadmin, name='marketingassignedadmin'),
    re_path(r'^marketingassignedshowadmin$', views.marketingassignedshowadmin, name='marketingassignedshowadmin'),
    re_path(r'^adminmarass2$', views.adminmarass2, name='adminmarass2'),

    re_path(r'^admintasksandproject1$', views.admintasksandproject1, name='admintasksandproject1'),
#    re_path(r'^admingivetask1$', views.admingivetask1, name='admingivetask1'),
    re_path(r'^admingivetask2$', views.admingivetask2, name='admingivetask2'),
    re_path(r'^adminviewtrainee$', views.adminviewtrainee, name='adminviewtrainee'),
    re_path(r'^admintraineedesi$', views.admintraineedesi, name='admintraineedesi'),



    re_path(r'^adminregistrationdetails2$', views.adminregistrationdetails2, name='adminregistrationdetails2'),


    re_path(r'^loadhremployeess1$', views.loadhremployeess1, name='loadhremployeess1'),
    re_path(r'^loadadmindesi$', views.loadadmindesi, name='loadadmindesi'),
    re_path(r'^adminloademployeess$', views.adminloademployeess, name='adminloademployeess'),
    re_path(r'^admintaskmanager$', views.admintaskmanager, name='admintaskmanager'),
    re_path(r'^givtaskadminadd$', views.givtaskadminadd, name='givtaskadminadd'),

    re_path(r'^proadminviewtrainee$', views.proadminviewtrainee, name='proadminviewtrainee'),
    re_path(r'^proadmintraineedesi$', views.proadmintraineedesi, name='proadmintraineedesi'),
    re_path(r'^proadminloademployeess$', views.proadminloademployeess, name='proadminloademployeess'),

    re_path(r'^seradminviewtrainee$', views.seradminviewtrainee, name='seradminviewtrainee'),
    re_path(r'^seradmintraineedesi$', views.seradmintraineedesi, name='seradmintraineedesi'),
    re_path(r'^seradminloademployeess$', views.seradminloademployeess, name='seradminloademployeess'),

    re_path(r'^recadminviewtrainee$', views.recadminviewtrainee, name='recadminviewtrainee'),
    re_path(r'^recadmintraineedesi$', views.recadmintraineedesi, name='recadmintraineedesi'),
    re_path(r'^recadminloademployeess$', views.recadminloademployeess, name='recadminloademployeess'),

    re_path(r'^viewbranch1admin$', views.viewbranch1admin, name='viewbranch1admin'),
    re_path(r'^viewbranch1admin1$', views.viewbranch1admin1, name='viewbranch1admin1'),
    re_path(r'^adminpregistrationdetails$', views.adminpregistrationdetails, name='adminpregistrationdetails'),
    re_path(r'^adminregistrationdetailsview$', views.adminregistrationdetailsview, name='adminregistrationdetailsview'),

    re_path(r'^adminregistrationdetailsedit$', views.adminregistrationdetailsedit, name='adminregistrationdetailsedit'),
    re_path(r'^updateregdetails$', views.updateregdetails, name='updateregdetails'),

    #re_path(r'^adminregistrationdetailsedit/(?P<id>\d+)$', views.adminregistrationdetailsedit, name='adminregistrationdetailsedit'),
    #re_path(r'^adminregistrationdetailsedit/updateregdetails/(?P<id>\d+)$', views.updateregdetails, name='updateregdetails'),
    re_path(r'^deleteregdetails/(?P<id>\d+)$', views.deleteregdetails, name='deleteregdetails'),

    re_path(r'^adminexperiencecertificate1$', views.adminexperiencecertificate1, name='adminexperiencecertificate1'),
    re_path(r'^adminexperiencecertificate2$', views.adminexperiencecertificate2, name='adminexperiencecertificate2'),

    re_path(r'^adminbranch11$', views.adminbranch11, name='adminbranch11'),
    re_path(r'^adminbranch2$', views.adminbranch2, name='adminbranch2'),

#    re_path(r'^adminattendance1$', views.adminattendance1, name='adminattendance1'),
    re_path(r'^adminhremp$', views.adminhremp, name='adminhremp'),
    re_path(r'^adminempdesi$', views.adminempdesi, name='adminempdesi'),

    re_path(r'^br$', views.br, name='br'),
    re_path(r'^br1$', views.br1, name='br1'),
    re_path(r'^br2$', views.br2, name='br2'),

    re_path(r'^adminattendance1$', views.adminattendance1, name='adminattendance1'),

    re_path(r'^regi1$', views.regi1, name='regi1'),
    re_path(r'^at2$', views.at2, name='at2'),
    re_path(r'^reg2$', views.reg2, name='reg2'),
    re_path(r'^seradmintraineedesi1$', views.seradmintraineedesi1, name='seradmintraineedesi1'),
    re_path(r'^seradminloademployeess1$', views.seradminloademployeess1, name='seradminloademployeess1'),
    re_path(r'^admintaskmanager1$', views.admintaskmanager1, name='admintaskmanager1'),


    re_path(r'^viewbranch1showadmin$', views.viewbranch1showadmin, name='viewbranch1showadmin'),
    re_path(r'^admintraineebranch1$', views.admintraineebranch1, name='admintraineebranch1'),
    re_path(r'^admintraineebranch2$', views.admintraineebranch2, name='admintraineebranch2'),

    re_path(r'^adminexperiecnceedit/(?P<id>\d+)$', views.adminexperiecnceedit,name='adminexperiecnceedit'),
    re_path(r'^adminexperiecnceedit/updateexperiencedetails/(?P<id>\d+)$', views.updateexperiencedetails,name='updateexperiencedetails'),

    re_path(r'^ex$', views.ex,name='ex'),

    re_path(r'^adminattendance2$', views.adminattendance2, name='adminattendance2'),
    re_path(r'^adminputmanagerattendance$', views.adminputmanagerattendance, name='adminputmanagerattendance'),
    re_path(r'^managerattendanceadd$', views.managerattendanceadd, name='managerattendanceadd'),
    re_path(r'^adminmanagerattendance1$', views.adminmanagerattendance1, name='adminmanagerattendance1'),
    re_path(r'^adminmanagerattendance11$', views.adminmanagerattendance11, name='adminmanagerattendance11'),
    re_path(r'^adminmanageratte11$', views.adminmanageratte11, name='adminmanageratte11'),
    re_path(r'^adminattenmy$', views.adminattenmy, name='adminattenmy'),
    re_path(r'^adminattenmy11$', views.adminattenmy11, name='adminattenmy11'),
    re_path(r'^adminattenmy112$', views.adminattenmy112, name='adminattenmy112'),


    re_path(r'^adminleaveapplication1$', views.adminleaveapplication1, name='adminleaveapplication1'),
    re_path(r'^adminleaveapplication2$', views.adminleaveapplication2, name='adminleaveapplication2'),

    re_path(r'^adminemployeeattendance1$', views.adminemployeeattendance1, name='adminemployeeattendance1'),
    re_path(r'^adminempatte$', views.adminempatte, name='adminempatte'),
    re_path(r'^empat2$', views.empat2, name='empat2'),
    re_path(r'^adminempatteshow$', views.adminempatteshow, name='adminempatteshow'),
    re_path(r'^adminmanageratte1$', views.adminmanageratte1, name='adminmanageratte1'),
    re_path(r'^adminempatte1$', views.adminempatte1, name='adminempatte1'),

    re_path(r'^adminmanageinternship1$', views.adminmanageinternship1, name='adminmanageinternship1'),
#    re_path(r'^admininternshipview$', views.admininternshipview, name='admininternshipview'),

    re_path(r'^adminempbranch1$', views.adminempbranch1, name='adminempbranch1'),
    re_path(r'^adminempman1$', views.adminempman1, name='adminempman1'),
    re_path(r'^adminemphr1$', views.adminemphr1, name='adminemphr1'),
    re_path(r'^adminempde1$', views.adminempde1, name='adminempde1'),
    re_path(r'^adminempdes1$', views.adminempdes1, name='adminempdes1'),

    re_path(r'^adminrepbranch$', views.adminrepbranch, name='adminrepbranch'),
    re_path(r'^adminrepbranch1$', views.adminrepbranch1, name='adminrepbranch1'),
    re_path(r'^rep1$', views.rep1, name='rep1'),
    re_path(r'^adminprobranch1$', views.adminprobranch1, name='adminprobranch1'),
    re_path(r'^adminprobranch2$', views.adminprobranch2, name='adminprobranch2'),
    re_path(r'^admintaskbranch1$', views.admintaskbranch1, name='admintaskbranch1'),
    re_path(r'^admintaskbranch2$', views.admintaskbranch2, name='admintaskbranch2'),

    re_path(r'^admintrabranchatt1$', views.admintrabranchatt1, name='admintrabranchatt1'),
    re_path(r'^admintrabranchatt11$', views.admintrabranchatt11, name='admintrabranchatt11'),

    re_path(r'^admintrabranchper1$', views.admintrabranchper1, name='admintrabranchper1'),
    re_path(r'^adminsylbranch1$', views.adminsylbranch1, name='adminsylbranch1'),
    re_path(r'^adminsy$', views.adminsy, name='adminsy'),
    re_path(r'^adminsylbranch2$', views.adminsylbranch2, name='adminsylbranch2'),

    re_path(r'^adminhrattendance1$', views.adminhrattendance1, name='adminhrattendance1'),
    re_path(r'^adminhratte1$', views.adminhratte1, name='adminhratte1'),

    re_path(r'^searchadmin$', views.searchadmin, name='searchadmin'),
    #path('searchadmin/',views.Blogsearchadmin,name='searchadmin')

    re_path(r'^addpandse$', views.addpandse, name='addpandse'),
    re_path(r'^s$', views.s, name='s'),
    re_path(r'^dynamic_articles_view$', views.dynamic_articles_view, name='dynamic_articles_view'),
    re_path(r'^dynamic_articles_view1$', views.dynamic_articles_view1, name='dynamic_articles_view1'),

    re_path(r'^adminassigned1$', views.adminassigned1, name='adminassigned1'),
    re_path(r'^adminempdes11$', views.adminempdes11, name='adminempdes11'),

    re_path(r'^adminempper1$', views.adminempper1, name='adminempper1'),
    re_path(r'^adminempper2$', views.adminempper2, name='adminempper2'),

    re_path(r'^addProduct$', views.addProduct, name='addProduct'),
    re_path(r'^indexxxx$', views.indexxxx, name='indexxxx'),
    re_path(r'^editProduct/(?P<id>\d+)$', views.editProduct, name='editProduct'),

    re_path(r'^viewProduct/(?P<id>\d+)$', views.viewProduct, name='viewProduct'),

    re_path(r'^GeneratePdf$', views.GeneratePdf.as_view(), name='GeneratePdf'),
    re_path(r'^GeneratePDF$', views.GeneratePDF.as_view(), name='GeneratePDF'),

    re_path(r'^ViewPDF$', views.ViewPDF.as_view(), name='ViewPDF'),
    re_path(r'^DownloadPDF$', views.DownloadPDF.as_view(), name='DownloadPDF'),

    re_path(r'^render_to_pdf$', views.render_to_pdf, name='render_to_pdf'),

    re_path(r'^GeneratePdf2$', views.GeneratePdf2.as_view(), name='GeneratePdf2'),
    #re_path(r'^GeneratePDF2$', views.GeneratePDF2.as_view(), name='GeneratePDF2'),

    re_path(r'^fetch_resources$', views.fetch_resources, name='fetch_resources'),
    re_path(r'^render_to_pdf3$', views.render_to_pdf3, name='render_to_pdf3'),

    re_path(r'^GeneratePdf3$', views.GeneratePdf3.as_view(), name='GeneratePdf3'),

    re_path(r'^render_pdf_view11$', views.render_pdf_view11, name='render_pdf_view11'),

    re_path(r'^newid$', views.newid, name='newid'),

    re_path(r'^qr$', views.qr, name='qr'),

    re_path(r'^addqr$', views.addqr, name='addqr'),

    re_path(r'^ViewPDFreg$', views.ViewPDFreg.as_view(), name='ViewPDFreg'),

    re_path(r'^viewProductreg/(?P<id>\d+)$', views.viewProductreg, name='viewProductreg'),



#-----------------------------------add!
    re_path(r'^adminregistrationdetailsview1/(?P<id>\d+)$', views.adminregistrationdetailsview1, name='adminregistrationdetailsview1'),
    re_path(r'^adminregistrationdetailsview1/updateregdetailsview/(?P<id>\d+)$', views.updateregdetailsview, name='updateregdetailsview'),

    # re_path(r'^qrnew$', views.qrnew, name='qrnew'),

    # re_path(r'^qradd$', views.qradd, name='qradd'),
    # re_path(r'^qrshow$', views.qrshow, name='qrshow'),

    re_path(r'^pie_chart$', views.pie_chart, name='pie_chart'),
    #re_path(r'^population_chart$', views.population_chart, name='population_chart'),
#---------------------
    re_path(r'^adminpie_chart$', views.adminpie_chart, name='adminpie_chart'),
    re_path(r'^adminbar_chart$', views.adminbar_chart, name='adminbar_chart'),
    re_path(r'^adminperformance2$', views.adminperformance2, name='adminperformance2'),
    re_path(r'^adminperinsert$', views.adminperinsert, name='adminperinsert'),
    re_path(r'^admintraperformance1$', views.admintraperformance1, name='admintraperformance1'),

    re_path(r'^adtask2$', views.adtask2, name='adtask2'),
    re_path(r'^adminat2$', views.adminat2, name='adminat2'),



    re_path(r'^adminregnew$', views.adminregnew, name='adminregnew'),
    re_path(r'^adminregnewadd$', views.adminregnewadd, name='adminregnewadd'),

#    re_path(r'^adminpassword$', views.adminpassword, name='adminpassword'),

    re_path(r'^adminpassword/(?P<id>\d+)$', views.adminpassword, name='adminpassword'),
    re_path(r'^adminpassword/updateadminpassword/(?P<id>\d+)$', views.updateadminpassword, name='updateadminpassword'),
    re_path(r'^adminregsmall$', views.adminregsmall, name='adminregsmall'),

    re_path(r'^admingiveproject1$', views.admingiveproject1, name='admingiveproject1'),
    re_path(r'^adproject2$', views.adproject2, name='adproject2'),
    re_path(r'^giveprojrctadminadd$', views.giveprojrctadminadd, name='giveprojrctadminadd'),
    re_path(r'^adminMANmyproject$', views.adminMANmyproject, name='adminMANmyproject'),
    re_path(r'^adminMANmyprojectsubtask$', views.adminMANmyprojectsubtask, name='adminMANmyprojectsubtask'),
    re_path(r'^adminMANMyprojectsubtaskProjectstatus$', views.adminMANMyprojectsubtaskProjectstatus, name='adminMANMyprojectsubtaskProjectstatus'),



    re_path(r'^one$', views.one, name='one'),

    re_path(r'^qrshowres$', views.qrshowres, name='qrshowres'),
    re_path(r'^qrnotres$', views.qrnotres, name='qrnotres'),
    re_path(r'^new$', views.new, name='new'),

    re_path(r'^please$', views.please, name='please'),
    re_path(r'^up$', views.up, name='up'),
    re_path(r'^v$', views.v, name='v'),
    re_path(r'^logindp$', views.logindp, name='logindp'),
    re_path(r'^homesec$', views.homesec, name='homesec'),
    re_path(r'^logout$', views.logout, name='logout'),


#---------------Bibin Section------------------------------------------------------

    re_path(r'^MANmarketing$', views.MANmarketing, name='MANmarketing'),
    re_path(r'^MANPromarketing$', views.MANPromarketing, name='MANPromarketing'),
    re_path(r'^manpromarketadd$', views.manpromarketadd, name='manpromarketadd'),
    re_path(r'^MANservices$', views.MANservices, name='MANservices'),
    re_path(r'^MANrecru$', views.MANrecru, name='MANrecru'),
    re_path(r'^manrecruadd$', views.manrecruadd, name='manrecruadd'),



#---------------Marketing Section------------------------------------------------------#

]