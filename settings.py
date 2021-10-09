from tkinter import *
from PIL import Image, ImageTk
from db_conn import *

def settings(email):
    global settings_screen
    global settings_icon
    global back_icon
    global type_btn_hide_name
    global type_btn_hide_photo
    global hide_username_on
    global hide_photo_on
    global btn_hide_name
    global btn_hide_photo
    global off
    global on

    settings_screen = Toplevel()
    settings_icon = ImageTk.PhotoImage(Image.open("settings.png").resize((80, 80), Image.ANTIALIAS))
    back_icon = ImageTk.PhotoImage(Image.open("arrow_back.png").resize((50,50), Image.ANTIALIAS))
    on = PhotoImage(file = "on.png")
    off = PhotoImage(file = "off.png")
    hide_username_on = False 
    hide_photo_on = False

    txt_title = "E-Book System"
    geometry_size = "1366x768"
    txt_settings = "Settings"
    txt_hide_name = "Hide your name"
    txt_hide_name_definition = getNameDefinition(email)
    txt_hide_profile_pic = "Hide your profile picture"
    txt_hide_profile_pic_definition = "No one is allowed to view your profile picture"
    type_btn_hide_name = "hideUsername"
    type_btn_hide_photo = "hideProfilePicture"

    lbl_back = Label(settings_screen, image = back_icon, cursor="hand2")
    lbl_back.place(x=80, y=40)
    lbl_back.bind("<Button-1>", lambda e: delete_settings_screen())
    Label(settings_screen, image = settings_icon).place(x=130, y=100)
    Label(settings_screen, text = txt_settings, font = ("Helvetica", 14, "bold")).place(x=230, y = 130)
    Label(settings_screen, text = txt_hide_name, font = ("Helvetica", 12, "bold")).place(x=180, y = 230)
    Label(settings_screen, text = txt_hide_name_definition, foreground = "blue", font = ("Helvetica", 12)).place(x=180, y = 260)
   # btn_hide_name = Button(settings_screen, image=off, bd=0, command= updateUserSetting(email,type_btn_hide_name, hide_username_on)).place(x=300, y=205)
    btn_hide_name = Button(settings_screen, image=off, bd=0).place(x=700, y=235)
    Label(settings_screen, text = txt_hide_profile_pic, font = ("Helvetica", 12, "bold")).place(x=180, y = 300)
    Label(settings_screen, text = txt_hide_profile_pic_definition, foreground = "blue", font = ("Helvetica", 12)).place(x=180, y = 330)
    #btn_hide_photo = Button(settings_screen, image=off, bd=0, command= updateUserSetting(email,type_btn_hide_photo, hide_photo_on)).place(x=300, y=275)
    btn_hide_photo = Button(settings_screen, image=off, bd=0).place(x=700, y=305)

    #getUserSetting(email)

    settings_screen.title(txt_title)
    settings_screen.state("zoomed")
    settings_screen.geometry(geometry_size)

def getNameDefinition(email):
    dbQuery = "SELECT username FROM dbo.Users WITH(NOLOCK) WHERE email = '"+email+"'"
    result = readFromDb(dbQuery)
    definition = result[0] +" to " + result[0][:1]+"********"+result[0][-1]
    return definition

def delete_settings_screen():
    settings_screen.destroy()

def getUserSetting(email):
    dbQuery = """SELECT S.Name AS SettingName, US.isActive AS Active
                 FROM dbo.Settings S WITH(NOLOCK) 
                 INNER JOIN dbo.UserSetting US WITH(NOLOCK) ON US.SettingId = S.Id
				 INNER JOIN dbo.Users U WITH(NOLOCK) ON U.Id = US.UserId AND U.email = '"""+email+"""'"""
    result = readAllFromDb(dbQuery)

    for row in result:
        if row.SettingName == type_btn_hide_name:
            if row.Active == 1:
                hide_username_on = True
        elif row.SettingName == type_btn_hide_photo:
            if row.Active == 1:
                hide_photo_on = True
    switch()

def updateUserSetting(email, settingName, active):
    dbQuery1 ="""UPDATE dbo.UserSetting
            SET isActive = 1
            WHERE SettingId = (
                                SELECT Id FROM dbo.Settings WITH(NOLOCK)
                                WHERE Name = '"""+settingName+"""'
                                )
            AND UserId = (
                            SELECT Id FROM dbo.Users WITH(NOLOCK)
                            WHERE email = '"""+email+"""'
                            )"""

    dbQuery0 ="""UPDATE dbo.UserSetting
                SET isActive = 0
                WHERE SettingId = (
                                    SELECT Id FROM dbo.Settings WITH(NOLOCK)
                                    WHERE Name = '"""+settingName+"""'
                                  )
                AND UserId = (
                                SELECT Id FROM dbo.Users WITH(NOLOCK)
                                WHERE email = '"""+email+"""'
                             )"""
    
    if settingName == type_btn_hide_name:
        if active:
            insertUpdateDeleteToDb(dbQuery0)
            hide_username_on = False
        else:
            insertUpdateDeleteToDb(dbQuery1)
            hide_username_on = True
    elif settingName == type_btn_hide_photo:
        if active:
            insertUpdateDeleteToDb(dbQuery0)
            hide_photo_on = False
        else:
            insertUpdateDeleteToDb(dbQuery1)
            hide_photo_on = True
    switch()

def switch():
        if hide_username_on:
            btn_hide_name.config(image=on)
        else:
            btn_hide_name.config(image=off)
        
        if hide_photo_on:
            btn_hide_photo.config(image=on)
        else:
            btn_hide_photo.config(image=off)
