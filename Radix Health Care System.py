from tkinter import *
from tkinter import messagebox

log=Tk()
logos=PhotoImage(file='fixed orange.png')
#-----------------------------------------------------------

def startingpage():
    
    def othr_labs():
        
        def laboratory():
            
            screen=Tk()
            screen.title("LABORATORY")

            screen.geometry("1255x944")

            

            mainframe=Frame(screen,bg="white",width="1300",height="1200")
            mainframe.place(x=1,y=1)
            Pic=PhotoImage(file="laboratory.png")
            imagelabel=Label(mainframe,text="R A D I X   L A B O R A T O R Y",font=("Times New Roman",40),fg="BLUE",bg="white")
            imagelabel.place(x=275,y=20)


            

            

            def cal():
                root=Tk()
                root.title("Laboratory Calculator")
                root.geometry("1255x944")
                imagelabel=Label(root,text="R A D I X   L A B O R A T O R Y   CALCULATOR ",font=("Times New Roman",40),fg="BLUE",bg="white")
                imagelabel.place(x=78,y=20)
                entry=Entry(root,font=("Times New Roman",20))
                entry.place(x=480,y=140)

                label=Label(root,font=("Times New Roman",20))
                def bill():
                    
                    label.config(text='Rs.'+str(eval(entry.get())))
                    label.place(x=580,y=240)
                button=Button(root,text="GENERATE BILL",font=("Times New Roman",20),command=bill,bg="blue",fg="white")
                button.place(x=500,y=190)
                

                firsttest=Label(root,text="1.CBC(Rs.1200)",font="Bold",bg="blue",fg="white",width=40,height=2)
                firsttest.place(x=11,y=350)



                secondtest=Label(root,text="2.LFT(Rs.1400)",font="Bold",bg="blue",fg="white",width=40,height=2)
                secondtest.place(x=11,y=410)



                thirdtest=Label(root,text="3.CHOLESTROL(Rs.1800)",bg="blue",fg="white",font="Bold",width=40,height=2)
                thirdtest.place(x=11,y=470)




                fourthtest=Label(root,text="4.Basic THyroid Profile(FT3,FT4,TSH(Rs.2000))",bg="blue",fg="white",font="Bold",width=40,height=2)
                fourthtest.place(x=11,y=530)




                fifthtest=Label(root,text="5.lipid Profile(Coronary risk panel(Rs.800))",font="Bold",bg="blue",fg="white",width=40,height=2)
                fifthtest.place(x=11,y=590)




                sixtest=Label(root,text="6. Semen Analysis(Rs.900)",font="Bold",bg="blue",fg="white",width=40,height=2)
                sixtest.place(x=11,y=650)

                seventest=Label(root,text="7.RFT(Rs.1100)",font="Bold",bg="blue",fg="white",width=40,height=2)
                seventest.place(x=390,y=350)




                eighttest=Label(root,text="8.Uric Acid(Rs.1700)",bg="blue",fg="white",font="Bold",width=40,height=2)
                eighttest.place(x=390,y=410)
                    
                        

                    
            def run():

                    
                name.delete(0,END)
                age.delete(0,END)
                teste.delete(0,END)#(Will clear data entering tabs after saving or registering patient)


                    
                patientname=namepatient.get()
                patientage=patage.get()
                requiredtest=patest.get()
                


                file=open("5.txt","a")#(It will add patients to database.)
                file.write(f"\n{patientname},{patientage},{requiredtest}")
                file.close()
                
                messagebox.showinfo("RADIX LABORATORY!","A patient has been registered successfully")
                

                    
                
                   
                    
                    
            namepatient=StringVar()
            patage=IntVar()
            patest=IntVar()
            patientname=Label(mainframe,text="Patientname*",font="Bold")
            patientname.place(x=25,y=193)
            name=Entry(mainframe,textvar=namepatient,width="40",bd="1")
            name.place(x=45,y=230)
            patientage=Label(mainframe,text="Patientage*",font="Bold")
            patientage.place(x=25,y=260)
            age=Entry(mainframe,textvar=patage,width="40",bd="1")
            age.place(x=45,y=310)
            test=Label(mainframe,text=" Required Test*",font="Bold")
            test.place(x=300,y=193)
            teste=Entry(mainframe,textvar=patest,width="40",bd="1")
            teste.place(x=305,y=230)





                         


                            





            firsttest=Label(mainframe,text="1.CBC(complete blood count)",font="Bold",bg="blue",fg="white",width=30,height=6)
            firsttest.place(x=11,y=370)



            secondtest=Label(mainframe,text="2.LFT(liver function tests)",font="Bold",bg="blue",fg="white",width=30,height=6)
            secondtest.place(x=320,y=370)



            thirdtest=Label(mainframe,text="3.CHOLESTROL",bg="blue",fg="white",font="Bold",width=30,height=6)
            thirdtest.place(x=631,y=370)




            fourthtest=Label(mainframe,text="4.Basic THyroid Profile(FT3,FT4,TSH)",bg="blue",fg="white",font="Bold",width=30,height=6)
            fourthtest.place(x=941,y=370)




            fifthtest=Label(mainframe,text="5.lipid Profile(Coronary risk panel)",font="Bold",bg="blue",fg="white",width=30,height=6)
            fifthtest.place(x=11,y=520)




            sixtest=Label(mainframe,text="6. Semen Analysis",font="Bold",bg="blue",fg="white",width=30,height=6)
            sixtest.place(x=320,y=520)

            seventest=Label(mainframe,text="RFT",font="Bold",bg="blue",fg="white",width=30,height=6)
            seventest.place(x=631,y=520)




            eighttest=Label(mainframe,text="8.Uric Acid",bg="blue",fg="white",font="Bold",width=30,height=6)
            eighttest.place(x=941,y=520)



                        




                       




            register=Button(mainframe,text="REGISTER",font=('Times New Roman',12),width=10,command=run,bg="blue",fg="white")
            register.place(x=320,y=310)

            register=Button(mainframe,text="GENERATE BILL",font=('Times New Roman',12),width=25,bg="blue",fg="white",command=cal)
            register.place(x=640,y=310)
        
        
        
        def Blood_Donations():
            
            def blood_req():
                
                def boek():
                    screen.destroy()
                    
                screen=Tk()

                screen.title("Blood Bank")
                screen.geometry("700x700")
                screen.resizable(width=False,height=False)
                outers=Frame(screen,width=407,height=418,bg='white')
                my_Label=Label(outers,text=" RADIX BLOOD BANK",font=("Times New Roman",20),fg="black",bg="red",width="80",height="2")
                my_Label.pack()


                def patient_savers():
                    required=blood.get()
                    import pandas as pd

                    redix=pd.read_csv("3.txt")
                    search=redix.loc[(redix['BLOOD']==required)]
                    if len(search)!=0:
                        messagebox.showinfo("RADIX BLOOD BANK","WE can help you by required blood group reach our laboratory soon.")
                    if len(search)==0:
                        messagebox.showerror("RADIX BLOOD BANK","SORRY!We cannot help you by required blood group ")
        

        

            

                    
                   

                namedonor=StringVar()
                agedonor=StringVar()
                bloodgroup=StringVar()
                namelabel=Label(outers,text="Enter Patient Name*",font="Bold")
                namelabel.place(x=250,y=135)
                name=Entry(outers,textvar=namedonor,width="40",bd=1)

                name.place(x="250",y="165")

                agelabel=Label(outers,text=" Enter Patient Age*",font="Bold")
                agelabel.place(x=250,y=195)
                    
                age=Entry(outers,textvar=agedonor,width="40")

                age.place(x="250",y="225")

                grouplabel=Label(outers,text="Enter Required Bloodgroup*",font="Bold")
                grouplabel.place(x=250,y=255)    
                blood=Entry(outers,textvar=bloodgroup,width="40")


                blood.place(x="250",y="285")



                save=Button(outers,text="Search",font="Bold",bg="red",fg="white",command=patient_savers)
                save.place(x="280",y="340")

                beeq=Button(outers,text="Back",font="Bold",bg="red",fg="white",command=boek)
                beeq.place(x=250,y=390)


                outers.pack(fill=BOTH,expand=TRUE)
            
                
            def blood_don():
                
                def boek():
                    screen.destroy()
                    
                screen=Tk()

                screen.title("Blood Bank")
                screen.geometry("700x700")
                screen.resizable(width=False,height=False)
                outers=Frame(screen,width=407,height=418,bg='white')
                my_Label=Label(outers,text=" RADIX BLOOD BANK",font=("Times New Roman",20),fg="black",bg="red",width="80",height="2")
                my_Label.pack()




                    
                   

                namedonor=StringVar()
                agedonor=StringVar()
                bloodgroup=StringVar()
                namelabel=Label(outers,text="Enter Donor Name*",font="Bold")
                namelabel.place(x=250,y=135)
                name=Entry(outers,textvar=namedonor,width="40",bd=1)

                name.place(x="250",y="165")

                agelabel=Label(outers,text=" Enter Donor Age*",font="Bold")
                agelabel.place(x=250,y=195)
                    
                age=Entry(outers,textvar=agedonor,width="40")

                age.place(x="250",y="225")

                grouplabel=Label(outers,text="Enter Bloodgroup*",font="Bold")
                grouplabel.place(x=250,y=255)    
                blood=Entry(outers,textvar=bloodgroup,width="40")


                blood.place(x="250",y="285")



                save=Button(outers,text="Save Donor Information!",font="Bold",bg="red",fg="white")
                save.place(x="280",y="340")

                beeq=Button(outers,text="Back",font="Bold",bg="red",fg="white",command=boek)
                beeq.place(x=250,y=390)


                outers.pack(fill=BOTH,expand=TRUE)
                
            
            def back_to_menu():
                bloodlab.destroy()
            bloodlab=Tk()
            bloodlab.geometry('900x600')
            
            bloodframe=Frame(bloodlab)
            bloodframe.pack(expand=TRUE,fill=BOTH)



            specifybelowradixlabel=Label(bloodframe,text='Choose To Donate or Get Blood',font=('Drexs',30))
            specifybelowradixlabel.pack(pady=15)

            specown=Button(bloodframe,height=2,width=27,text='Blood Donation',bg='#ED7020',fg='white',font=('Orbitron',12),command=blood_don)
            specown.pack(pady=15)

            specadmin=Button(bloodframe,height=2,width=27,text='Blood Required',bg='#ED7020',fg='white',font=('Orbitron',12),command=blood_req)
            specadmin.pack(pady=15)


            backing_button_to_welcome_page=Button(bloodframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_menu)
            backing_button_to_welcome_page.pack()
            
        def financ():
            import pyttsx3
            a=pyttsx3.init()
            a.say("You have to Fill the form on your browser, Make sure the Internet is available!")
            a.runAndWait()
            import webbrowser
            webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSdTXzpXcrbZk6GrbgAXgiQmFQkAhyjyhXK_MLSRCPgthGJXzw/viewform?usp=sf_link")

          
            
        
        
        def back_to_welcome_pg():
            loglab.destroy()
            
        loglab=Tk()
        loglab.geometry('900x600')
        
        labsframe=Frame(loglab)
        labsframe.pack(expand=TRUE,fill=BOTH)



        specifybelowradixlabel=Label(labsframe,text='Select Labs/Donation Facilities',font=('Drexs',30))
        specifybelowradixlabel.pack(pady=15)

        specown=Button(labsframe,height=2,width=27,text='Blood Donation',bg='#ED7020',fg='white',font=('Orbitron',12),command=Blood_Donations)
        specown.pack(pady=15)
      
        specadmin=Button(labsframe,height=2,width=27,text='Laboratory',bg='#ED7020',fg='white',font=('Orbitron',12),command=laboratory)
        specadmin.pack(pady=15)
        
        specfinan=Button(labsframe,height=2,width=27,text='Financial Assistance',bg='#ED7020',fg='white',font=('Orbitron',12),command=financ)
        specfinan.pack(pady=15)


        backing_button_to_welcome_page=Button(labsframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_welcome_pg)
        backing_button_to_welcome_page.pack()
        
    
    
    def specifying():
        pleaseselect.forget()
        loginselection.forget()
        othermenus.forget()
        def back_to_wc():
            specifyingframe.destroy()
            radixlogo.destroy()
            specifybelowradixlabel.destroy()
            specown.destroy()
            specadmin.destroy()
            specdoc.destroy()
            backing_button_to_welcome_page.destroy()
            startingpage()
        
        
        def doc_prtl():
            specifyingframe.destroy()
            radixlogo.destroy()
            specifybelowradixlabel.destroy()
            specown.destroy()
            specadmin.destroy()
            specdoc.destroy()
            backing_button_to_welcome_page.destroy()
            
            framedisown=Frame(log)
            framedisown.pack(fill=BOTH,expand=TRUE)
            def clear_display_of_doc_pr():
                framedisown.destroy()
                mytext.destroy()
                infoidlabel.destroy()
                infoid.destroy()
                infopslabel.destroy()
                infops.destroy()
                searchbutton.destroy()
                clearbutton.destroy()
                backbut.destroy()
                doc_prtl()
            
            def back_to_speci_frm_doc():
                framedisown.destroy()
                mytext.destroy()
                infoidlabel.destroy()
                infoid.destroy()
                infopslabel.destroy()
                infops.destroy()
                searchbutton.destroy()
                clearbutton.destroy()
                backbut.destroy()
                specifying()
            
            def doc_creds():
                DocID=infoid.get()
                DocPass=infops.get()
                import pandas as pd
                pd.set_option('display.expand_frame_repr', False)
                file=pd.read_csv("AddDoc.txt")
                valid1=file.loc[(file['Password']==DocPass) & (file['Doctor ID']==DocID)]
                if len(valid1)==0:
                    messagebox.showinfo("","No Doctor Found!")
                else:
                    name=None
                    with open ("AddDoc.txt","r") as blast:
                        lines=(line1.rstrip() for line1 in blast)
                        lines=list(line1 for line1 in lines if line1)
                        for line in lines:
                            pat3=line.split(",")
                            if pat3[1]==DocID and pat3[2]==DocPass:
                                name=pat3[0]
                    def DocDat():
                        import pandas as hey
                        hey.set_option('display.expand_frame_repr', False)
                        ca=hey.read_csv("AddDoc.txt")
                        prin=ca.loc[ca["Doctor ID"]==DocID]
                        if len(prin)==0:
                            import sys
                            sys.stdout = open("data.txt", "w")

                            print("No Doctor Found")

                            sys.stdout.close()
                            
                        else:
                            import sys
                            sys.stdout = open("data.txt", "w")

                            print(prin)

                            sys.stdout.close()
                            
                           
                    def DocPat():

                        import pandas as pey
                        pey.set_option('display.expand_frame_repr', False)
                        ca=pey.read_csv("AdmittedPatientsDataBase.txt")
                        prin=ca.loc[ca['Under Supervision']==name]
                        if len(prin)==0:
                            import sys
                            sys.stdout = open("data.txt", "a")

                            print(f"No Active Patient under Supervision of {name}:- ")

                            sys.stdout.close()
                            
                        else:
                            import sys
                            sys.stdout = open("data.txt", "a")

                            print(prin)

                            sys.stdout.close()
                    import sys        
                    sys.stdout = open("data.txt", "a")

                    print()

                    sys.stdout.close()
                            
                    DocDat()
                    import sys
                    sys.stdout = open("data.txt", "w")

                    print("----------------------------------------------------------")
                    sys.stdout.close()
                    
                    import sys
                    sys.stdout = open("data.txt", "w")

                    print(f"Active Patients Under {name}.")
                    sys.stdout.close()
                    
                    
                    DocPat()
                    
                    infofile=open("data.txt","r")
                    stuff=infofile.read()
                    
                    mytext.insert(END,stuff)
                    infofile.close()
            mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
            mytext.pack(ipady=150,ipadx=400)
            infoidlabel=Label(framedisown,text='Enter Email')
            infoidlabel.pack()
            infoid=Entry(framedisown,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
            infoid.pack()
             
            
            infopslabel=Label(framedisown,text='Enter Password')
            infopslabel.pack()
            infops=Entry(framedisown,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
            infops.pack()
            
            
            searchbutton=Button(framedisown,width=35,pady=7,text='Login and View',bg='#ED7020',fg='white',border=0,command=doc_creds)
            searchbutton.pack(pady=5)

            clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display_of_doc_pr)
            clearbutton.pack(pady=5)

            backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_speci_frm_doc)
            backbut.pack(pady=5)
            
            
        
        def loginpage():
            #destroy precious contents
            specifyingframe.destroy()
            radixlogo.destroy()
            specifybelowradixlabel.destroy()
            specown.destroy()
            specadmin.destroy()
            specdoc.destroy()
            backing_button_to_welcome_page.destroy()
            
            
            
            #new page prefrences
            log.title("Signin")
            log.configure(bg='white')
            log.geometry('925x600')
            log.resizable(False,False)
            #------------------------------------------------------------
            def back():
                loginlogo.forget()
                UserNameBoxLabel.forget()
                username.forget()
                PasswordBoxLabel.forget()
                psswrd.forget()
                signinbutton.forget()
                backtomainpage.forget()
                frame1.forget()
                specifying()
            def owner_loggingin():
                """Owner Login"""
                b=username.get()
                c=psswrd.get()
                import pandas as pd
                ca=pd.read_csv("OwnerLogin.txt")
                prin=ca.loc[(ca['Email']==b) & (ca["Password"]==c)]
                if len(prin)==0:
                    messagebox.showinfo("","Incorrect Email/Password")
                else:
                    def owners_portal():
                        loginlogo.forget()
                        UserNameBoxLabel.forget()
                        username.forget()
                        PasswordBoxLabel.forget()
                        psswrd.forget()
                        signinbutton.forget()
                        backtomainpage.forget()
                        frame1.forget()
                        ownersframe=Frame(log)
                        ownersframe.pack(fill=BOTH,expand=TRUE)
                        def logout_of_owner():
                           ownersframe.destroy()
                           welcome_owner.destroy()
                           go_to_add_remove_doc.destroy()
                           go_to_Doctor_Supervision.destroy()
                           go_to_info.destroy()
                           logout_owner.destroy()
                           loginpage()
                        

                        def search_and_display_records():
                            ownersframe.destroy()
                            welcome_owner.destroy()
                            go_to_add_remove_doc.destroy()
                            go_to_view_database.destroy()
                            go_to_info.destroy()
                            go_to_Doctor_Supervision.destroy()
                            logout_owner.destroy()
                            
                            
                            
                            
                            
                            framedisown=Frame(log)
                            framedisown.pack(fill=BOTH,expand=TRUE)
                            
                            def search_and_display():
                                ID=infoid.get()

                                import pandas as hey
                                hey.set_option('display.expand_frame_repr', False)
                                ba=hey.read_csv("AddDoc.txt")
                                search1=ba.loc[ba['Doctor ID']==ID]
                                if len(search1)==0:
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr", False)
                                    pa=pd.read_csv("AdmittedPatientsDataBase.txt")
                                    search2=pa.loc[pa["Patient ID"]==ID]
                                    if len(search2)==0:
                                        import pandas as pc
                                        pc.set_option("display.expand_frame_repr", False)
                                        ca=pc.read_csv("CurrentAdmin.txt")
                                        search3=ca.loc[ca["Admin ID"]==ID]
                                        if len(search3)==0:
                                            import pandas as pf
                                            pf.set_option('display.expand_frame_repr', False)
                                            ta=pf.read_csv("CurrentNW.txt")
                                            search4=ta.loc[ta['N/W ID']==ID]
                                            if len(search4)==0:
                                                import sys
                                                sys.stdout = open("data.txt", "w")
                                                print("Data Not Found")
                                                sys.stdout.close()
                                            else:
                                                import sys
                                                sys.stdout = open("data.txt", "w")
                                                print(search4)
                                                sys.stdout.close()    
                                        else:
                                            import sys
                                            sys.stdout = open("data.txt", "w")
                                            print(search3)
                                            sys.stdout.close()
                                    else:
                                        import sys
                                        sys.stdout = open("data.txt", "w")
                                        print(search2)
                                        sys.stdout.close()
                                else:
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(search1)
                                    sys.stdout.close()
                                infofile=open("data.txt","r")
                                stuff=infofile.read()
                                
                                mytext.insert(END,stuff)
                                infofile.close()
                            def back_to_owner_portal():
                                framedisown.destroy()
                                mytext.destroy()
                                infoidlabel.destroy()
                                infoid.destroy()
                                searchbutton.destroy()
                                clearbutton.destroy()
                                backbut.destroy()
                                owners_portal()
                                
                            def clear_display():
                                framedisown.destroy()
                                mytext.destroy()
                                infoidlabel.destroy()
                                infoid.destroy()
                                searchbutton.destroy()
                                clearbutton.destroy()
                                backbut.destroy()
                                search_and_display_records()
                            
                             
                            mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                            mytext.pack(ipady=150,ipadx=400)
                            infoidlabel=Label(framedisown,text='Enter ID of Person')
                            infoidlabel.pack()
                            infoid=Entry(framedisown,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                            infoid.pack()


                            searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=search_and_display)
                            searchbutton.pack(pady=5)

                            clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                            clearbutton.pack(pady=5)

                            backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_owner_portal)
                            backbut.pack(pady=5)
                        
                        def add_ya_remove_admin():#ADD REMOVE ADMIN
                            ownersframe.destroy()
                            welcome_owner.destroy()
                            go_to_add_remove_doc.destroy()
                            go_to_view_database.destroy()
                            go_to_info.destroy()
                            go_to_add_remove_admin.destroy()
                            go_to_Doctor_Supervision.destroy()
                            go_to_add_remove_worker.destroy()
                            
                            
                            
                            def for_adding_admin():
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                
                                
                                
                                log=Tk()
                                log.geometry('800x600')
                                log.title('Add Admin')





                                def adding_admin_to_data():
                                    with open("CurrentAdmin.txt","r") as hey:
                                        d=hey.readlines()
                                        a=adnameentry.get()
                                        b=adidentry.get()
                                        b1=adaccpasswordentry.get()
                                        d=adgenderentry.get()
                                        c=adcityentry.get()
                                        f=adcontactentry.get()
                                        e=adaddressentry.get()
                                        with open("CurrentAdmin.txt","a") as bye:
                                            if len(d)==0:
                                                bye.write(f"{a},{b},{b1},{d},{c},{f},{e}")
                                            else:
                                                bye.write(f"\n{a},{b},{b1},{d},{c},{f},{e}")
                                        messagebox.showinfo("","Admin Added Successfully")


                                def back_frm_ading_admin():
                                    log.destroy()
                                    add_ya_remove_admin()



                                addremoveframe=Frame(log)
                                addremoveframe.pack(fill=BOTH,expand=TRUE)




                                label_for_add_remove=Label(addremoveframe,text='Enter Admin Info to Add in database',font=('Drexs',23))
                                label_for_add_remove.pack()

                                adname=Label(addremoveframe,text='Admin Name')
                                adname.pack()
                                adnameentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                adnameentry.pack()



                                adid=Label(addremoveframe,text='Admin ID')
                                adid.pack()
                                adidentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                adidentry.pack()


                                adaccpassword=Label(addremoveframe,text='Account Password')
                                adaccpassword.pack()
                                adaccpasswordentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                adaccpasswordentry.pack()

                                adgender=Label(addremoveframe,text='Gender')
                                adgender.pack()
                                adgenderentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                adgenderentry.pack()



                                adcity=Label(addremoveframe,text='City')
                                adcity.pack()
                                adcityentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                adcityentry.pack()


                                adcontact=Label(addremoveframe,text='Contact')
                                adcontact.pack()
                                adcontactentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                adcontactentry.pack()



                                adaddress=Label(addremoveframe,text='Address')
                                adaddress.pack()
                                adaddressentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                adaddressentry.pack()






                                adadddoctorbutton=Button(addremoveframe,width=35,pady=7,text='Add Admin',bg='#ED7020',fg='white',border=0,command=adding_admin_to_data)
                                adadddoctorbutton.pack(pady=10)

                                adbackadding=Button(addremoveframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_frm_ading_admin)
                                adbackadding.pack()
                            
                            def for_deleting_admin():
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                log=Tk()
                                log.geometry('800x600')
                                log.title('Remove Admin')
                                removeadminframe=Frame(log)
                                removeadminframe.pack(expand=TRUE,fill=BOTH)





                                def admin_deleter():
                                    docnum=removingadminIDEntry.get()
                                    with open ("CurrentAdmin.txt","r") as pat1:
                                        lines=(line1.rstrip() for line1 in pat1)
                                        lines=list(line1 for line1 in lines if line1)
                                        with open ("deletedAdmin.txt","a") as pat2:
                                            duration=removingadminDurationEntry.get()
                                            
                                            for line in lines:
                                                f=False
                                                pat3=line.split(",")
                                                if docnum==pat3[1] and docnum in pat3:
                                                    pat2.writelines(f"\n{line}"+","+f"{duration}")
                                                    messagebox.showinfo("","Admin Deleted!")
                                                    f=True
                                            if not f:
                                                messagebox.showinfo("","Pls enter correct Admin ID!")
                                                
                                    with open("CurrentAdmin.txt","r") as file:
                                        lines1=(line.rstrip() for line in file)
                                        lines1=list(line for line in lines1 if line)
                                        with open ("CurrentAdmin.txt","w") as file2:
                                            for line in lines1:
                                                liney=line.split(",")
                                                if liney[1]!=docnum:
                                                    file2.write(line+"\n")


                                def back_frm_deleting_an_admin():
                                    log.destroy()
                                    add_ya_remove_admin()
                                    




                                removeingadminlabel=Label(removeadminframe,text='Remove an Admin',font=('Drexs',23))
                                removeingadminlabel.pack(pady=10)


                                removingadminID=Label(removeadminframe,text='Enter Admin ID:')
                                removingadminID.pack()

                                removingadminIDEntry=Entry(removeadminframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                removingadminIDEntry.pack()



                                removingAdminDuration=Label(removeadminframe,text='Enter Duration Of Service:')
                                removingAdminDuration.pack()

                                removingadminDurationEntry=Entry(removeadminframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                removingadminDurationEntry.pack(pady=12)

                                removingAdminButton=Button(removeadminframe,width=35,pady=7,text='Delete Admin',bg='#ED7020',fg='white',border=0,command=admin_deleter)
                                removingAdminButton.pack(pady=12)

                                back_to_admin_ya=Button(removeadminframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_frm_deleting_an_admin)
                                back_to_admin_ya.pack()
                                
                                
                                
                                
                            
                            
                            def bck_to_owner_aftr_admin():
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                owners_portal()
                                
                            
                            
                            selectforaddremframe=Frame(log)
                            selectforaddremframe.pack(expand=TRUE,fill=BOTH)


                            ttle=Label(selectforaddremframe,text='Please Make Your Selection',font=('Drexs',23))
                            ttle.pack(pady=100)

                            add_selection=Button(selectforaddremframe,width=35,pady=7,text='Add Admin',bg='#ED7020',fg='white',border=0,command=for_adding_admin)
                            add_selection.pack(pady=11)


                            delete_selection=Button(selectforaddremframe,width=35,pady=7,text='Delete Admin',bg='#ED7020',fg='white',border=0,command=for_deleting_admin)
                            delete_selection.pack(pady=11)

                            not_selected_back=Button(selectforaddremframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=bck_to_owner_aftr_admin)
                            not_selected_back.pack()

                        def add_ya_remove():#ADD REMOVE DOCTOR
                            
                            ownersframe.destroy()
                            welcome_owner.destroy()
                            go_to_add_remove_doc.destroy()
                            go_to_info.destroy()
                            go_to_add_remove_admin.destroy()
                            go_to_view_database.destroy()
                            go_to_add_remove_worker.destroy()
                            go_to_Doctor_Supervision.destroy()
                            logout_owner.destroy()
                            
                            def Back_2_Owner():
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                owners_portal()
                                
                            
                            
                            
                            
                            def adddoctr():
                                log=Tk()
                                log.geometry('800x600')
                                log.title('Add Doctor')
                                
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                
                                
                                
                                
                                addremoveframe=Frame(log)
                                addremoveframe.pack(fill=BOTH,expand=TRUE)
                                
                                def back_from_adding_doctor():
                                    label_for_add_remove.destroy()
                                    docname.destroy()
                                    docnameentry.destroy()
                                    docid.destroy()
                                    docidentry.destroy()
                                    accpassword.destroy()
                                    accpasswordentry.destroy()
                                    city.destroy()
                                    cityentry.destroy()
                                    gender.destroy()
                                    genderentry.destroy()
                                    address.destroy()
                                    addressentry.destroy()
                                    contact.destroy()
                                    contactentry.destroy()
                                    ward.destroy()
                                    wardentry.destroy()
                                    qualification.destroy()
                                    qualificationentry.destroy()
                                    experience.destroy()
                                    experienceentry.destroy()
                                    adddoctorbutton.destroy()
                                    backadding.destroy()
                                    log.destroy()
                                    add_ya_remove()


                                def adding_doctor_in_database():
                                    with open("AddDoc.txt","r") as hey:
                                        d=hey.readlines()
                                        a=docnameentry.get()
                                        b=docidentry.get()
                                        b1=accpasswordentry.get()
                                        c=cityentry.get()
                                        d=genderentry.get()
                                        e=addressentry.get()
                                        f=contactentry.get()
                                        g=wardentry.get()
                                        h=qualificationentry.get()
                                        i=experienceentry.get()
                                        with open("AddDoc.txt","a") as bye:
                                            if len(d)==0:
                                                bye.write(f"{a},{b},{b1},{c},{d},{e},{f},{g},{h},{i}")
                                            else:
                                                bye.write(f"\n{a},{b},{b1},{c},{d},{e},{f},{g},{h},{i}")
                                        print("Doctor Added Successfully")


                                label_for_add_remove=Label(addremoveframe,text='Enter Doctor Info to Add in database',font=('Drexs',23))
                                label_for_add_remove.pack()

                                docname=Label(addremoveframe,text='Doctor Name')
                                docname.pack()
                                docnameentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                docnameentry.pack()



                                docid=Label(addremoveframe,text='Doctor ID')
                                docid.pack()
                                docidentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                docidentry.pack()


                                accpassword=Label(addremoveframe,text='Account Password')
                                accpassword.pack()
                                accpasswordentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                accpasswordentry.pack()


                                city=Label(addremoveframe,text='City')
                                city.pack()
                                cityentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                cityentry.pack()

                                gender=Label(addremoveframe,text='Gender')
                                gender.pack()
                                genderentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                genderentry.pack()


                                address=Label(addremoveframe,text='Address')
                                address.pack()
                                addressentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                addressentry.pack()


                                contact=Label(addremoveframe,text='Contact')
                                contact.pack()
                                contactentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                contactentry.pack()


                                ward=Label(addremoveframe,text='Ward')
                                ward.pack()
                                wardentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                wardentry.pack()


                                qualification=Label(addremoveframe,text='Qualification')
                                qualification.pack()
                                qualificationentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                qualificationentry.pack()



                                experience=Label(addremoveframe,text='Experience')
                                experience.pack()
                                experienceentry=Entry(addremoveframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                experienceentry.pack(pady=10)


                                adddoctorbutton=Button(addremoveframe,width=35,pady=7,text='Add Doctor',bg='#ED7020',fg='white',border=0,command=adding_doctor_in_database)
                                adddoctorbutton.pack(pady=10)

                                backadding=Button(addremoveframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_from_adding_doctor)
                                backadding.pack()
                            
                            
                            def we_selected_delete():
                                log=Tk()
                                log.geometry('800x600')
                                log.title('Remove Doctor')
                                
                                
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                
                                deletingframe=Frame(log)
                                deletingframe.pack(expand=TRUE,fill=BOTH)


                                def Back_From_Deleting():
                                    deletingframe.destroy()
                                    label_for_remove.destroy()
                                    Label_For_ID.destroy()
                                    Entry_For_ID.destroy()
                                    Remove_Button.destroy()
                                    Back_After_Deleting.destroy()
                                    log.destroy()
                                    add_ya_remove()
                                    
                                    
                                    
                                    

                                def delete_doctor_record():
                                    docnum=Entry_For_ID.get()
                                    with open ("AddDoc.txt","r") as pat1:
                                        lines=(line1.rstrip() for line1 in pat1)
                                        lines=list(line1 for line1 in lines if line1)
                                        with open ("DeleteDoc.txt","a") as pat2:
                                            
                                            for line in lines:
                                                f=False
                                                pat3=line.split(",")
                                                if docnum==pat3[1] and docnum in pat3:
                                                    pat2.writelines(f"\n{line}")
                                                    print("Doctor Deleted!")
                                                    f=True
                                            if not f:
                                                print("Pls enter correct Doctor ID")
                                                
                                    with open("AddDoc.txt","r") as file:
                                        lines1=(line.rstrip() for line in file)
                                        lines1=list(line for line in lines1 if line)
                                        with open ("AddDoc.txt","w") as file2:
                                            for line in lines1:
                                                liney=line.split(",")
                                                if liney[1]!=docnum:
                                                    file2.write(line+"\n")
                                    




                                label_for_remove=Label(deletingframe,text='Enter Doctor ID to Remove',font=('Drexs',23))
                                label_for_remove.pack(pady=30)


                                Label_For_ID=Label(deletingframe,text='Doctor ID')
                                Label_For_ID.pack()

                                Entry_For_ID=Entry(deletingframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                Entry_For_ID.pack(pady=11)

                                Remove_Button=Button(deletingframe,width=35,pady=7,text='Remove Doctor',bg='#ED7020',fg='white',border=0,command=delete_doctor_record)
                                Remove_Button.pack(pady=11)

                                Back_After_Deleting=Button(deletingframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=Back_From_Deleting)
                                Back_After_Deleting.pack()
                            
                            
                            selectforaddremframe=Frame(log)
                            selectforaddremframe.pack(expand=TRUE,fill=BOTH)


                            ttle=Label(selectforaddremframe,text='Please Make Your Selection',font=('Drexs',23))
                            ttle.pack(pady=100)

                            add_selection=Button(selectforaddremframe,width=35,pady=7,text='Add Doctor',bg='#ED7020',fg='white',border=0,command=adddoctr)
                            add_selection.pack(pady=11)


                            delete_selection=Button(selectforaddremframe,width=35,pady=7,text='Delete Doctor',bg='#ED7020',fg='white',border=0,command=we_selected_delete)
                            delete_selection.pack(pady=11)

                            not_selected_back=Button(selectforaddremframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=Back_2_Owner)
                            not_selected_back.pack()
                        
                        def add_ya_remove_workers():#ADD REMOVE WORKER
                            ownersframe.destroy()
                            welcome_owner.destroy()
                            go_to_add_remove_doc.destroy()
                            go_to_view_database.destroy()
                            go_to_info.destroy()
                            go_to_add_remove_admin.destroy()
                            go_to_add_remove_worker.destroy()
                            go_to_Doctor_Supervision.destroy()
                            selectforaddremframe=Frame(log)
                            selectforaddremframe.pack(expand=TRUE,fill=BOTH)
                            
                            def go_to_oner_portal():
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                owners_portal()
                                
                            
                            def wantd_to_add_worker():
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                
                                
                                log=Tk()
                                log.geometry('900x600')
                                log.title('Add Worker/Nurse')
                                addwrkrframe=Frame(log)
                                addwrkrframe.pack(expand=TRUE,fill=BOTH)


                                def we_added_nurs():
                                    with open("CurrentNW.txt","r") as hey:
                                        d=hey.readlines()
                                        a=nursename.get()
                                        a1=nursdesig.get()
                                        b=nurseID.get()
                                        b1=nursepassword.get()
                                        d=nursegender.get()
                                        c=nursecity.get()
                                        f=nursecontact.get()
                                        e=nurseaddress.get()
                                        with open("CurrentNW.txt","a") as bye:
                                            if len(d)==0:
                                                bye.write(f"{a},{a1},{b},{b1},{d},{c},{f},{e}")
                                            else:
                                                bye.write(f"\n{a},{a1},{b},{b1},{d},{c},{f},{e}")
                                        messagebox.showinfo("","Worker/Nurse Added Successfully")

                                def back_to_add_del_nurse():
                                    addwrkrframe.destroy()
                                    addwrkerLabel.destroy()
                                    nursenamelabel.destroy()
                                    nursename.destroy()
                                    nursedesiglabel.destroy()
                                    nursdesig.destroy()
                                    nurseIDlabel.destroy()
                                    nurseID.destroy()
                                    nursepasslabel.destroy()
                                    nursepassword.destroy()
                                    nursegenderlabel.destroy()
                                    nursegender.destroy()
                                    nursecitylabel.destroy()
                                    nursecity.destroy()
                                    nursecontactlabel.destroy()
                                    nursecontact.destroy()
                                    nurseaddress.destroy()
                                    addingbuttonofwrk.destroy()
                                    bckbutton.destroy()
                                    log.destroy()
                                    add_ya_remove_workers()


                                addwrkerLabel=Label(addwrkrframe,text='Adding Nurse/Worker',font=('Drexs',23))
                                addwrkerLabel.pack()

                                nursenamelabel=Label(addwrkrframe,text='Nurse/worker Name:')
                                nursenamelabel.pack()
                                nursename=Entry(addwrkrframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                nursename.pack()



                                nursedesiglabel=Label(addwrkrframe,text='Designation:')
                                nursedesiglabel.pack()

                                nursdesig=Entry(addwrkrframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                nursdesig.pack()

                                nurseIDlabel=Label(addwrkrframe,text='Nurse/Worker ID')
                                nurseIDlabel.pack()

                                nurseID=Entry(addwrkrframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                nurseID.pack()


                                nursepasslabel=Label(addwrkrframe,text='Account Password:')
                                nursepasslabel.pack()



                                nursepassword=Entry(addwrkrframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                nursepassword.pack()


                                nursegenderlabel=Label(addwrkrframe,text='Gender:')
                                nursegenderlabel.pack()

                                nursegender=Entry(addwrkrframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                nursegender.pack()

                                nursecitylabel=Label(addwrkrframe,text='Enter City:')
                                nursecitylabel.pack()


                                nursecity=Entry(addwrkrframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                nursecity.pack()

                                nursecontactlabel=Label(addwrkrframe,text='Contact:')
                                nursecontactlabel.pack()

                                nursecontact=Entry(addwrkrframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                nursecontact.pack()

                                nurseaddresslabel=Label(addwrkrframe,text='Address:')
                                nurseaddresslabel.pack()


                                nurseaddress=Entry(addwrkrframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                nurseaddress.pack(pady=10)   


                                addingbuttonofwrk=Button(addwrkrframe,width=35,pady=7,text='Add Worker/Nurse',bg='#ED7020',fg='white',border=0,command=we_added_nurs)
                                addingbuttonofwrk.pack(pady=10)



                                bckbutton=Button(addwrkrframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_add_del_nurse)
                                bckbutton.pack()
                            
                            def wantd_to_delete_worker():
                                selectforaddremframe.destroy()
                                ttle.destroy()
                                add_selection.destroy()
                                delete_selection.destroy()
                                not_selected_back.destroy()
                                
                                
                                log=Tk()
                                log.geometry('800x600')
                                log.title('Remove Worker')
                                removeadminframe=Frame(log)
                                removeadminframe.pack(expand=TRUE,fill=BOTH)





                                def worker_deleter():
                                    docnum=removingadminIDEntry.get()
                                    with open ("CurrentNW.txt","r") as pat1:
                                        lines=(line1.rstrip() for line1 in pat1)
                                        lines=list(line1 for line1 in lines if line1)
                                        with open ("DeletedNW.txt","a") as pat2:
                                            duration=removingadminDurationEntry.get()
                                            f=False
                                            for line in lines:
                                                
                                                pat3=line.split(",")
                                                if docnum==pat3[2] and docnum in pat3:
                                                    pat2.writelines(f"\n{line}"+f"{duration}")
                                                    messagebox.showinfo("","Worker/Nurse Deleted!")
                                                    f=True
                                            if not f:
                                                messagebox.showinfo("","Please Enter Correct Info!")
                                                
                                    with open("CurrentNW.txt","r") as file:
                                        lines1=(line.rstrip() for line in file)
                                        lines1=list(line for line in lines1 if line)
                                        with open ("CurrentNW.txt","w") as file2:
                                            for line in lines1:
                                                liney=line.split(",")
                                                if liney[2]!=docnum:
                                                    file2.write(line+"\n")


                                def back_frm_deleting_an_admin():
                                    log.destroy()
                                    add_ya_remove_workers()
                                    




                                removeingadminlabel=Label(removeadminframe,text='Remove Worker/Nurse',font=('Drexs',23))
                                removeingadminlabel.pack(pady=10)


                                removingadminID=Label(removeadminframe,text='Enter Worker ID:')
                                removingadminID.pack()

                                removingadminIDEntry=Entry(removeadminframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                removingadminIDEntry.pack()



                                removingAdminDuration=Label(removeadminframe,text='Enter Duration Of Service:')
                                removingAdminDuration.pack()

                                removingadminDurationEntry=Entry(removeadminframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                                removingadminDurationEntry.pack(pady=12)

                                removingAdminButton=Button(removeadminframe,width=35,pady=7,text='Delete Worker/Nurse',bg='#ED7020',fg='white',border=0,command=worker_deleter)
                                removingAdminButton.pack(pady=12)

                                back_to_admin_ya=Button(removeadminframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_frm_deleting_an_admin)
                                back_to_admin_ya.pack()


                            ttle=Label(selectforaddremframe,text='Please Make Your Selection',font=('Drexs',23))
                            ttle.pack(pady=100)

                            add_selection=Button(selectforaddremframe,width=35,pady=7,text='Add Worker/Nurse',bg='#ED7020',fg='white',border=0,command=wantd_to_add_worker)
                            add_selection.pack(pady=11)


                            delete_selection=Button(selectforaddremframe,width=35,pady=7,text='Delete Worker/Nurse',bg='#ED7020',fg='white',border=0,command=wantd_to_delete_worker)
                            delete_selection.pack(pady=11)

                            not_selected_back=Button(selectforaddremframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=go_to_oner_portal)
                            not_selected_back.pack()
                            
                        def doc_is_supervising():#DOCTOR SUPERVISING
                            ownersframe.destroy()
                            welcome_owner.destroy()
                            go_to_add_remove_doc.destroy()
                            go_to_info.destroy()
                            go_to_Doctor_Supervision.destroy()
                            go_to_view_database.destroy()
                            logout_owner.destroy()





                            framedisown=Frame(log)
                            framedisown.pack(fill=BOTH,expand=TRUE)

                            def search_and_display():
                                name=infoid.get()
                                print("--------------------------------------------------------")
                                def DocDat():
                                    import pandas as hey
                                    hey.set_option('display.expand_frame_repr', False)
                                    ca=hey.read_csv("AddDoc.txt")
                                    prin=ca.loc[ca['Name']==name]
                                    if len(prin)==0:
                                        import sys
                                        sys.stdout = open("data.txt", "w")
                                        print("No Doctor Found")
                                        sys.stdout.close()
                                        infofile=open("data.txt","r")
                                        stuff=infofile.read()
                                        
                                        mytext.insert(END,stuff)
                                        infofile.close()
                                    else:
                                        import sys
                                        sys.stdout = open("data.txt", "w")
                                        print(prin)
                                        sys.stdout.close()
                                        infofile=open("data.txt","r")
                                        stuff=infofile.read()
                                        
                                        mytext.insert(END,stuff)
                                        infofile.close()
                                        
                                def DocPat():
                                    import pandas as hey
                                    hey.set_option('display.expand_frame_repr', False)
                                    ca=hey.read_csv("AdmittedPatientsDataBase.txt")
                                    prin=ca.loc[ca['Under Supervision']==name]
                                    if len(prin)==0:
                                        import sys
                                        sys.stdout = open("data.txt", "w")
                                        print(f"No Active Patient under Supervision of {name}:- ")
                                        sys.stdout.close()
                                        infofile=open("data.txt","r")
                                        stuff=infofile.read()
                                        
                                        mytext.insert(END,stuff)
                                        infofile.close()
                                    else:
                                        import sys
                                        sys.stdout = open("data.txt", "w")
                                        print(prin)
                                        sys.stdout.close()
                                        infofile=open("data.txt","r")
                                        stuff=infofile.read()
                                        
                                        mytext.insert(END,stuff)
                                        infofile.close()
                                        
                                DocDat()
                                import sys
                                sys.stdout = open("data.txt", "w")
                                print("-----------------------------" + f"Active Patients Under {name}:- ")
                                sys.stdout.close()
                                infofile=open("data.txt","r")
                                stuff=infofile.read()
                                
                                mytext.insert(END,stuff)
                                infofile.close()
                                
            
                                DocPat()
                                
                                
                            def back_to_owner_portal():
                                framedisown.destroy()
                                mytext.destroy()
                                infoidlabel.destroy()
                                infoid.destroy()
                                searchbutton.destroy()
                                clearbutton.destroy()
                                backbut.destroy()
                                owners_portal()
                                
                            def clear_display():
                                framedisown.destroy()
                                mytext.destroy()
                                infoidlabel.destroy()
                                infoid.destroy()
                                searchbutton.destroy()
                                clearbutton.destroy()
                                backbut.destroy()
                                search_and_display_records()

                             
                            mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                            mytext.pack(ipady=150,ipadx=400)
                            infoidlabel=Label(framedisown,text='Enter ID of Person')
                            infoidlabel.pack()
                            infoid=Entry(framedisown,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                            infoid.pack()


                            searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=search_and_display)
                            searchbutton.pack(pady=5)

                            clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                            clearbutton.pack(pady=5)

                            backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_owner_portal)
                            backbut.pack(pady=5)
        
                        def view_databases():#VIEW DATABASES
                            ownersframe.destroy()
                            welcome_owner.destroy()
                            go_to_add_remove_doc.destroy()
                            go_to_view_database.destroy()
                            go_to_info.destroy()
                            go_to_add_remove_admin.destroy()
                            go_to_add_remove_worker.destroy()
                            go_to_Doctor_Supervision.destroy()
                            databseframe=Frame(log)
                            databseframe.pack(expand=TRUE,fill=BOTH)
                            def back_2_owner_prtl():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                owners_portal()
                                

                            def crnpatients():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                
                                def view_crnt_pats():
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr",False)
                                    ca=pd.read_csv("AdmittedPatientsDataBase.txt")
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(ca)
                                    sys.stdout.close()
                                    infofile=open("data.txt","r")
                                    stuff=infofile.read()
                                    
                                    mytext.insert(END,stuff)
                                    infofile.close()
                                def back_to_databases():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    view_databases()

                                def clear_display():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    crnpatients()
                                    
                                framedisown=Frame(log)
                                framedisown.pack(fill=BOTH,expand=TRUE)
                                mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                                mytext.pack(ipady=150,ipadx=400)
                    


                                searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=view_crnt_pats)
                                searchbutton.pack(pady=5)

                                clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                                clearbutton.pack(pady=5)

                                backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_databases)
                                backbut.pack(pady=5)
                            def delpatients():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                def discharged_pats():
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr",False)
                                    ca=pd.read_csv("DischargedPatient.txt")
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(ca)
                                    sys.stdout.close()
                                    infofile=open("data.txt","r")
                                    stuff=infofile.read()

                                    mytext.insert(END,stuff)
                                    infofile.close()
                                def back_to_databases():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    view_databases()

                                def clear_display():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    delpatients()
                                    
                                framedisown=Frame(log)
                                framedisown.pack(fill=BOTH,expand=TRUE)
                                mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                                mytext.pack(ipady=150,ipadx=400)


                                searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=discharged_pats)
                                searchbutton.pack(pady=5)

                                clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                                clearbutton.pack(pady=5)

                                backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_databases)
                                backbut.pack(pady=5)
                            def crnadmins():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                
                                def search_crnt_admin():
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr",False)
                                    ca=pd.read_csv("CurrentAdmin.txt")
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(ca)
                                    sys.stdout.close()
                                    infofile=open("data.txt","r")
                                    stuff=infofile.read()
                                    
                                    mytext.insert(END,stuff)
                                    infofile.close()
                                    
                                    
                                
                                def back_to_databases():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    view_databases()

                                def clear_display():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    crnadmins()
                                    
                                framedisown=Frame(log)
                                framedisown.pack(fill=BOTH,expand=TRUE)
                                mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                                mytext.pack(ipady=150,ipadx=400)
                        
                                searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=search_crnt_admin)
                                searchbutton.pack(pady=5)

                                clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                                clearbutton.pack(pady=5)

                                backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_databases)
                                backbut.pack(pady=5)
                            def deletedadmins():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                
                                def view_deleted_admins():
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr",False)
                                    ca=pd.read_csv("deletedAdmin.txt")
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(ca)
                                    sys.stdout.close()
                                    infofile=open("data.txt","r")
                                    stuff=infofile.read()

                                    mytext.insert(END,stuff)
                                    infofile.close()
                                def back_to_databases():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    view_databases()

                                def clear_display():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    deletedadmins()
                                    
                                framedisown=Frame(log)
                                framedisown.pack(fill=BOTH,expand=TRUE)
                                mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                                mytext.pack(ipady=150,ipadx=400)


                                searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=view_deleted_admins)
                                searchbutton.pack(pady=5)

                                clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                                clearbutton.pack(pady=5)

                                backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_databases)
                                backbut.pack(pady=5)
                            def curentdocs():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                def view_current_docs():
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr",False)
                                    ca=pd.read_csv("AddDoc.txt")
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(ca)
                                    sys.stdout.close()
                                    infofile=open("data.txt","r")
                                    stuff=infofile.read()

                                    mytext.insert(END,stuff)
                                    infofile.close()
                                def back_to_databases():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    view_databases()

                                def clear_display():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    curentdocs()
                                    
                                framedisown=Frame(log)
                                framedisown.pack(fill=BOTH,expand=TRUE)
                                mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                                mytext.pack(ipady=150,ipadx=400)


                                searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=view_current_docs)
                                searchbutton.pack(pady=5)

                                clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                                clearbutton.pack(pady=5)

                                backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_databases)
                                backbut.pack(pady=5)
                            def deleteddocs():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                def view_deleted_docs():
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr",False)
                                    ca=pd.read_csv("DeleteDoc.txt")
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(ca)
                                    sys.stdout.close()
                                    infofile=open("data.txt","r")
                                    stuff=infofile.read()

                                    mytext.insert(END,stuff)
                                    infofile.close()
                                def back_to_databases():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    view_databases()

                                def clear_display():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    deleteddocs()
                                    
                                framedisown=Frame(log)
                                framedisown.pack(fill=BOTH,expand=TRUE)
                                mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                                mytext.pack(ipady=150,ipadx=400)


                                searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=view_deleted_docs)
                                searchbutton.pack(pady=5)

                                clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                                clearbutton.pack(pady=5)

                                backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_databases)
                                backbut.pack(pady=5)
                            def crnworkers1():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                def view_current_workers():
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr",False)
                                    ca=pd.read_csv("CurrentNW.txt")
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(ca)
                                    sys.stdout.close()
                                    infofile=open("data.txt","r")
                                    stuff=infofile.read()

                                    mytext.insert(END,stuff)
                                    infofile.close()
                                def back_to_databases():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    view_databases()

                                def clear_display():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    crnworkers1()
                                    
                                framedisown=Frame(log)
                                framedisown.pack(fill=BOTH,expand=TRUE)
                                mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                                mytext.pack(ipady=150,ipadx=400)


                                searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=view_current_workers)
                                searchbutton.pack(pady=5)

                                clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                                clearbutton.pack(pady=5)

                                backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_databases)
                                backbut.pack(pady=5)
                            def deletedworkers():
                                databseframe.destroy()
                                databseLabel.destroy()
                                crntpat.destroy()
                                delpats.destroy()
                                crnadmin.destroy()
                                deladmin.destroy()
                                crndoc.destroy()
                                deldocs.destroy()
                                crnworkers.destroy()
                                delworker.destroy()
                                bkbut.destroy()
                                def view_deleted_wrker_nurses():
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr",False)
                                    ca=pd.read_csv("DeletedNW.txt")
                                    import sys
                                    sys.stdout = open("data.txt", "w")
                                    print(ca)
                                    sys.stdout.close()
                                    infofile=open("data.txt","r")
                                    stuff=infofile.read()

                                    mytext.insert(END,stuff)
                                    infofile.close()
                                def back_to_databases():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    view_databases()

                                def clear_display():
                                    framedisown.destroy()
                                    mytext.destroy()
                                    searchbutton.destroy()
                                    clearbutton.destroy()
                                    backbut.destroy()
                                    deletedworkers()
                                    
                                framedisown=Frame(log)
                                framedisown.pack(fill=BOTH,expand=TRUE)
                                mytext=Text(framedisown,height=2,width=12,font=('Calibri Light',11))
                                mytext.pack(ipady=150,ipadx=400)


                                searchbutton=Button(framedisown,width=35,pady=7,text='Search',bg='#ED7020',fg='white',border=0,command=view_deleted_wrker_nurses)
                                searchbutton.pack(pady=5)

                                clearbutton=Button(framedisown,width=20,pady=7,text='Clear',bg='#ED7020',fg='white',border=0,command=clear_display)
                                clearbutton.pack(pady=5)

                                backbut=Button(framedisown,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_databases)
                                backbut.pack(pady=5)





                            databseLabel=Label(databseframe,text='Click to view Database',font=('Drexs',23))
                            databseLabel.pack(pady=20)

                            crntpat=Button(databseframe,width=35,pady=7,text='Current Patients',bg='#ED7020',fg='white',border=0,command=crnpatients)
                            crntpat.pack(pady=9)

                            delpats=Button(databseframe,width=35,pady=7,text='Delete Patients',bg='#ED7020',fg='white',border=0,command=delpatients)
                            delpats.pack(pady=9)

                            crnadmin=Button(databseframe,width=35,pady=7,text='Current Admin',bg='#ED7020',fg='white',border=0,command=crnadmins)
                            crnadmin.pack(pady=9)

                            deladmin=Button(databseframe,width=35,pady=7,text='Delete Admin',bg='#ED7020',fg='white',border=0,command=deletedadmins)
                            deladmin.pack(pady=9)

                            crndoc=Button(databseframe,width=35,pady=7,text='Current Doctors',bg='#ED7020',fg='white',border=0,command=curentdocs)
                            crndoc.pack(pady=9)

                            deldocs=Button(databseframe,width=35,pady=7,text='Deleted Doctors',bg='#ED7020',fg='white',border=0,command=deleteddocs)
                            deldocs.pack(pady=9)

                            crnworkers=Button(databseframe,width=35,pady=7,text='Curent Workers',bg='#ED7020',fg='white',border=0,command=crnworkers1)
                            crnworkers.pack(pady=9)

                            delworker=Button(databseframe,width=35,pady=7,text='Deleted Workers',bg='#ED7020',fg='white',border=0,command=deletedworkers)
                            delworker.pack(pady=9)

                            bkbut=Button(databseframe,width=20,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_2_owner_prtl)
                            bkbut.pack(pady=5)



                        welcome_owner=Label(ownersframe,text='Welcome! Owner Of Redix\nPlease Make Your Selection',font=('Drexs',23))
                        welcome_owner.pack(ipady=70)
                        
                        
                        
                        go_to_view_database=Button(ownersframe,width=35,pady=7,text='View Databases',bg='#ED7020',fg='white',border=0,command=view_databases)
                        go_to_view_database.pack(pady=10)
                        
                        go_to_Doctor_Supervision=Button(ownersframe,width=35,pady=7,text='Doctor Supervision',bg='#ED7020',fg='white',border=0,command=doc_is_supervising)
                        go_to_Doctor_Supervision.pack()
                        
                        go_to_add_remove_doc=Button(ownersframe,width=35,pady=7,text='Add/Remove Doctor',bg='#ED7020',fg='white',border=0,command=add_ya_remove)
                        go_to_add_remove_doc.pack(pady=11)
                        
                        go_to_add_remove_admin=Button(ownersframe,width=35,pady=7,text='Add/Remove Admin',bg='#ED7020',fg='white',border=0,command=add_ya_remove_admin)
                        go_to_add_remove_admin.pack(pady=4)
                        
                        go_to_add_remove_worker=Button(ownersframe,width=35,pady=7,text='Add/Remove Worker',bg='#ED7020',fg='white',border=0,command=add_ya_remove_workers)
                        go_to_add_remove_worker.pack(pady=15)
                        

                        go_to_info=Button(ownersframe,width=35,pady=7,text='See Info',bg='#ED7020',fg='white',border=0,command=search_and_display_records)
                        go_to_info.pack()

                        logout_owner=Button(ownersframe,width=20,pady=7,text='🔒Logout',bg='#ED7020',fg='white',border=0,command=logout_of_owner)
                        logout_owner.pack(pady=15)

                    owners_portal()
            def forget_password_email():
                
                
                def take_back_to_owner_login():
                    loginlogo.forget()
                    UserNameBoxLabel.forget()
                    username.forget()
                    PasswordBoxLabel.forget()
                    psswrd.forget()
                    signinbutton.forget()
                    backtomainpage.forget()
                    frame1.forget()
                    log.destroy()
                    loginpage()
                
                
                        
                        
                log=Tk()
                log.geometry('900x600')
                log.title('New Credentials')
                newcrdsframe=Frame(log)
                newcrdsframe.pack(expand=TRUE,fill=BOTH)

                toplabel=Label(newcrdsframe,text='Enter OTP Sent to\nsyednshah5@gmail.com',font=('Drexs',23))
                toplabel.pack(pady=18)

                newemaillabel=Label(newcrdsframe,text='Enter OTP')
                newemaillabel.pack()

                OTP=Entry(newcrdsframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                OTP.pack()


                
                
                import smtplib
                import ssl
                from email.message import EmailMessage
                import random
                value=random.randint(0,9)
                value1=random.randint(0,9)
                value2=random.randint(0,9)

                a="abcdefghijklmnopqrstuvwxyz"
                b=""
                for i in range(0,3):
                    c=random.choice(a)
                    b+=c
                otp=str(value)+str(value1)+str(value2)+b
                print(otp)
                email_sender = 'healthcere.radix@gmail.com'
                email_password = 'pvqdgoaumeaywbka'
                email_receiver = 'mianfaraz2002@gmail.com'
                subject = 'Radix Healthcare Portal Owner Info Change'
                body = f"""
                                Enter This Code In your Radix Portal   {otp}
                """
                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['Subject'] = subject
                em.set_content(body)
                context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())
                def OTP_checker():
                    def email_sendings():
                        def entering_new_email_password():
                            
                            def confirming():
                                email=newemail.get()
                                password=newpasswordentry.get()
                                number=newnumberentry.get()
                                with open ('OwnerLogin.txt',"w") as rite:
                                    rite.write("Email,Password,Number")
                                with open ("ownerLogin.txt","a") as rite1:
                                    rite1.write("\n"+email+","+password+","+number)
                                messagebox.showinfo("","Email/Password Changed")
                            
                            def back_to_owner_loggin_new():
                                loginlogo.forget()
                                UserNameBoxLabel.forget()
                                username.forget()
                                PasswordBoxLabel.forget()
                                psswrd.forget()
                                signinbutton.forget()
                                backtomainpage.forget()
                                frame1.forget()
                                log.destroy()
                                loginpage.desroy()
                                loginpage()

                            log=Tk()
                            log.geometry('900x600')
                            log.title('New Credentials')
                            newcrdsframe=Frame(log)
                            newcrdsframe.pack(expand=TRUE,fill=BOTH)

                            toplabel=Label(newcrdsframe,text='Enter New Email and Password',font=('Drexs',23))
                            toplabel.pack(pady=18)

                            newemaillabel=Label(newcrdsframe,text='New Email:')
                            newemaillabel.pack()

                            newemail=Entry(newcrdsframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                            newemail.pack()

                            newpasswordlabel=Label(newcrdsframe,text='New Password:')
                            newpasswordlabel.pack()

                            newpasswordentry=Entry(newcrdsframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                            newpasswordentry.pack(pady=12)
                            
                            newnumberlabel=Label(newcrdsframe,text='New Number:')
                            newnumberlabel.pack()
                            
                            newnumberentry=Entry(newcrdsframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                            newnumberentry.pack()

                            changeButton=Button(newcrdsframe,width=35,pady=7,text='Change',bg='#ED7020',fg='white',border=0,command=confirming)
                            changeButton.pack(pady=12)

                            backbutton=Button(newcrdsframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_owner_loggin_new)
                            backbutton.pack()
                        entering_new_email_password()
                    entry=OTP.get()
                    if entry==otp:
                        print("Now you can chamge your Info")
                        email_sendings()
                        
                            
                    else:
                        messagebox.showinfo("","Enter Correct OTP")
                
                changeButton=Button(newcrdsframe,width=35,pady=7,text='Ok',bg='#ED7020',fg='white',border=0,command=OTP_checker)
                changeButton.pack(pady=12)

                backbutton=Button(newcrdsframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=take_back_to_owner_login)
                backbutton.pack()
                
                
                
                
                
                
                
                 
            
            frame1=Frame(log)
            frame1.pack(expand=TRUE,fill=BOTH)
            loginlogo=Label(frame1,image=logos,border=0,bg='white')
            loginlogo.pack(pady=43)

            #username box prefrences
            UserNameBoxLabel=Label(frame1,text='Email')
            UserNameBoxLabel.pack(padx=77)
            
            username=Entry(frame1,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
            username.pack(pady=12)
            #Password Box Prefrences
            PasswordBoxLabel=Label(frame1,text='Password')
            PasswordBoxLabel.pack()
            psswrd=Entry(frame1,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12),show=('*'))
            psswrd.pack(pady=12)
            #-------------------------------------------------------------
            signinbutton=Button(frame1,width=35,pady=7,text='Sign in',bg='#ED7020',fg='white',border=0,command=owner_loggingin)
            signinbutton.pack()
            #--------------------------------------------------------------
            #Forget button
            frgetbutton=Label(frame1,text='Forgot Passowrd',cursor="hand2",foreground="Blue",font= ('Aerial',9))
            frgetbutton.pack()
            frgetbutton.bind("<Button-1>", lambda e:forget_password_email())
            
            
            
            #Go Back Button
            backtomainpage=Button(frame1,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back)
            backtomainpage.pack(pady=8)
        
        def admins_login():
            specifyingframe.destroy()
            radixlogo.destroy()
            specifybelowradixlabel.destroy()
            specown.destroy()
            specadmin.destroy()
            specdoc.destroy()
            backing_button_to_welcome_page.destroy()
            screen1=Tk()
            screen1.title("ADMIN LOGIN")

            screen1.geometry("900x600")






            # Pic=PhotoImage(file="fixed orange.png")
            # imagelabel=Label(screen1,image=Pic,bg="white",text="bold")
            # imagelabel.pack(pady=14)


                
            def back_to_speci():
                screen1.destroy()
                specifying()
                
            def  enter():

                

                adid=emailentry.get()
                pw=passentry.get()
                import pandas as pd
                pd.set_option("display.expand_frame_repr", False)
                ca=pd.read_csv("CurrentAdmin.txt")
                prin=ca.loc[ca["Admin ID"]==adid]
                if len(prin)==0:
                    messagebox.showinfo("Incorrect Credentials!")
                else:
                    import pandas as cd
                    cd.set_option("display.expand_frame_repr", False)
                    cb=cd.read_csv("CurrentAdmin.txt")
                    prin1=cb.loc[cb["Password"]==pw]
                    if len(prin1)==0:
                        messagebox.showinfo("Incorrect Credentials!")
                    else:
                        display=Tk()
                        display.geometry('900x600')
                        
                        def add_patie():
                            screen=Tk()
                            screen.title("ADD PATIENT")

                            screen.geometry("1255x944")






                            Pic=PhotoImage(file="fixed orange.png")
                            imagelabel=Label(image=Pic,bg="white",text="bold")
                            imagelabel.place(x=460,y=30)

                            def back_to_add_rem_pat():
                                screen.destroy()
                                
                                

                                
                            def PatientAdmitHistory():
                                
                                with open("AdmittedPatientsDataBase.txt","r") as hey:
                                    a=firstentry.get()
                                    h=secondentry.get()
                                    
                                    i=twentyentry.get()
                                    j=thirdentry.get()
                                    k=fourthentry.get()
                                    l=fifthentry.get()
                                    m=sixthentry.get()
                                    n=seventhentry.get()
                                    
                                    b=eigthentry.get()
                                    c=thirtyentry.get()
                                    d=nineentry.get()
                                    e=tenthentry.get()
                                    
                                    f=elevenentry.get()
                                    import pandas as pd
                                    pd.set_option("display.expand_frame_repr", False)
                                    ca=pd.read_csv("AddDoc.txt")
                                    prin=ca.loc[ca['Name']==n]
                                    if len(prin)==0:
                                        
                                        messagebox.showinfo("ADMIN PORTAL","Doctor Not in DataBase")
                                        
                                    else:
                                        with open("AdmittedPatientsDataBase.txt","a") as bye:
                                            import datetime
                                            bye.write(f"\n{a},{h},{i},{j},{k},{l},{m},{n},{b},{c},{d},{e},{f},"+"Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
                                       
                                        messagebox.showinfo("ADMIN PORTAL","Patient Admitted Successfully!")
                                        

                                

                            firstlabel=Label(screen,text="Patient Name*",font="bold")
                            firstlabel.place(x=300,y=100)
                            Patientname=StringVar()
                            firstentry=Entry(screen,textvar=Patientname,font="bold",width="30")
                            firstentry.place(x=320,y=135)


                            secondlabel=Label(screen,text="Patient Id*",font="bold")
                            secondlabel.place(x=300,y=170)
                            PatientID=StringVar()
                            secondentry=Entry(screen,textvar=PatientID,font="bold",width="30")
                            secondentry.place(x=320,y=205)



                            secondlabel=Label(screen,text="City*",font="bold")
                            secondlabel.place(x=300,y=240)
                            city=StringVar()
                            twentyentry=Entry(screen,textvar=city,font="bold",width="30")
                            twentyentry.place(x=320,y=275)

                            thirdlabel=Label(screen,text="Gender*",font="bold")
                            thirdlabel.place(x=300,y=310)
                            Gender=StringVar()
                            thirdentry=Entry(screen,textvar=Gender,font="bold",width="30")
                            thirdentry.place(x=320,y=345)


                            fourthlabel=Label(screen,text="Address*",font="bold")
                            fourthlabel.place(x=300,y=380)
                            address=StringVar()
                            fourthentry=Entry(screen,textvar=address,font="bold",width="30")
                            fourthentry.place(x=320,y=415)


                            fifthlabel=Label(screen,text="Contact*",font="bold")
                            fifthlabel.place(x=300,y=440)
                            contact=IntVar()
                            fifthentry=Entry(screen,textvar=contact,font="bold",width="30")
                            fifthentry.place(x=320,y=475)


                            sixthlabel=Label(screen,text="Ward*",font="bold")
                            sixthlabel.place(x=300,y=510)
                            ward=StringVar()
                            sixthentry=Entry(screen,textvar=ward,font="bold",width="30")
                            sixthentry.place(x=320,y=545)


                            seventhlabel=Label(screen,text="UnderSupervision*",font="bold")
                            seventhlabel.place(x=300,y=580)
                            supervision=StringVar()
                            seventhentry=Entry(screen,textvar=supervision,font="bold",width="30")
                            seventhentry.place(x=320,y=615)

                            eigthlabel=Label(screen,text="Complaints/Disease*",font="bold")
                            eigthlabel.place(x=300,y=640)
                            complaints=StringVar()
                            eigthentry=Entry(screen,textvar=complaints,font="bold",width="30")
                            eigthentry.place(x=320,y=675)


                            eigthlabel=Label(screen,text="Allergies*",font="bold")
                            eigthlabel.place(x=620,y=100)
                            allergies=StringVar()
                            thirtyentry=Entry(screen,textvar=allergies,font="bold",width="30")
                            thirtyentry.place(x=640,y=135)


                            ninelabel=Label(screen,text="Surgeries*",font="bold")
                            ninelabel.place(x=620,y=170)
                            Surgery=StringVar()
                            nineentry=Entry(screen,textvar=Surgery,font="bold",width="30")
                            nineentry.place(x=640,y=205)

                            tenthlabel=Label(screen,text="Immunization*",font="bold")
                            tenthlabel.place(x=620,y=240)
                            immunization=StringVar()
                            tenthentry=Entry(screen,textvar=immunization,font="bold",width="30")
                            tenthentry.place(x=640,y=275)


                            elevenlabel=Label(screen,text="Drugs*",font="bold")
                            elevenlabel.place(x=620,y=310)
                            drugs=StringVar()
                            elevenentry=Entry(screen,textvar=drugs,font="bold",width="30")
                            elevenentry.place(x=640,y=345)


                            regbutton=Button(screen,text="REGISTER",font="bold",bg="orange",fg="black",width="20",height="1",command=PatientAdmitHistory)
                            regbutton.place(x=680,y=390)

                            backb=Button(screen,text="Go Back",font="bold",bg="orange",fg="black",width="20",height="1",command=back_to_add_rem_pat)
                            backb.place(x=680,y=430)
                            
                        def delete_patie():
                            
                            
                            
                            def discharg_mechanish():
                                patnum=removingpatIDEntry.get()
                                stay=removingpatDurationEntry.get()
                                with open ("AdmittedPatientsDataBase.txt","r") as pat1:
                                    lines=(line1.rstrip() for line1 in pat1)
                                    lines=list(line1 for line1 in lines if line1)
                                    with open ("DischargedPatient.txt","a") as pat2:
                                        f=False
                                        for line in lines:
                                            pat3=line.split(",")
                                            if patnum==pat3[1] and patnum in pat3:
                                                import datetime
                                                pat2.writelines(f"\n{line}"+"," + stay+"Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
                                                messagebox.showinfo("ADMIN PORTAL","Patient Discharged!")
                                                f=True
                                        if not f:
                                            messagebox.showinfo("Please Enter Correct Info!")
                                            
                                with open("AdmittedPatientsDataBase.txt","r") as file:
                                    lines1=(line.rstrip() for line in file)
                                    lines1=list(line for line in lines1 if line)
                                    with open ("AdmittedPatientsDataBase.txt","w") as file2:
                                        for line in lines1:
                                            liney=line.split(",")
                                            if liney[1]!=patnum:
                                                file2.write(line+"\n")
                            
                            def back_from_discharging():
                                displaydelpat.destroy()
                                
                            
                            displaydelpat=Tk()
                            displaydelpat.geometry('900x600')
                            delpatframe=Frame(displaydelpat)
                            delpatframe.pack()
                            
                            
                            removeingpatlabel=Label(delpatframe,text='Remove Patient',font=('Drexs',23))
                            removeingpatlabel.pack(pady=10)
                            
                            removingpatID=Label(delpatframe,text='Enter Patient Number:')
                            removingpatID.pack()
                            
                            removingpatIDEntry=Entry(delpatframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                            removingpatIDEntry.pack()
                            
                            removingpatDuration=Label(delpatframe,text='Enter Duration of Stay:')
                            removingpatDuration.pack()
                            
                            removingpatDurationEntry=Entry(delpatframe,bd=1,width=27,bg='white',highlightbackground='blue',highlightcolor='blue',font=('Calibri Light',12))
                            removingpatDurationEntry.pack(pady=12)
                            
                            removingpatButton=Button(delpatframe,width=35,pady=7,text='Discharge Patient',bg='#ED7020',fg='white',border=0,command=discharg_mechanish)
                            removingpatButton.pack(pady=12)
                            
                            back_to_pat_ya=Button(delpatframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_from_discharging)
                            back_to_pat_ya.pack()
                            
                            
                            
                            
                            
                            
                        
                        
                        def back_to_admin_loggin():
                            display.destroy()
                            
                            
                        
                        imagelabel=Label(display,text="R A D I X",font=("Times New Roman",40),fg="orange",bg="white")
                        imagelabel.place(x=450,y=20)


                        welcomelabel=Label(display,text="Welcome Admin Of Radix",font=("Bookman Old Style",20),fg="black")
                        welcomelabel.place(x=400,y=130)

                        welcomelabel=Label(display,text="Please Make Your Selection",font=("Bookman Old Style",20),fg="black")
                        welcomelabel.place(x=390,y=175)

                        addbutton=Button(display,text="Add the patient",fg="white",bg="orange",width="35",height="2",font="bold",command=add_patie)
                        addbutton.place(x=400,y=260)

                        removebutton=Button(display,text="Remove the patient",fg="white",bg="orange",width="35",height="2",font="bold",command=delete_patie)
                        removebutton.place(x=400,y=320)

                        logout=Button(display,text="Logout",fg="white",bg="orange",height="1",font="bold",command=back_to_admin_loggin)
                        logout.place(x=530,y=380)
                    






                    

                    





                
            emaillabel=Label(screen1,text="Email",font="bold")
            emaillabel.pack()

            emailadmin=StringVar()
            emailentry=Entry(screen1,textvar=emailadmin,width="40",bd="1")
            emailentry.pack()


            passlabel=Label(screen1,text="Password",font="bold")
            passlabel.pack()

            passadmin=StringVar()

            passentry=Entry(screen1,textvar=passadmin,width="40",show="*",bd="1")
            passentry.pack(pady=12)


            signin=Button(screen1,text="Signin",font="bold",width="26",height="1",fg="white",bg="orange",command=enter)
            signin.pack(pady=7)
            
            bac=Button(screen1,text="Back",font="bold",width="12",height="1",fg="white",bg="orange",command=back_to_speci)
            bac.pack()
            
        specifyingframe=Frame(log)
        specifyingframe.pack(expand=TRUE,fill=BOTH)


        radixlogo=Label(specifyingframe,image=logos)
        radixlogo.pack()

        specifybelowradixlabel=Label(specifyingframe,text='Go to Your Concerned Portal',font=('Drexs',30))
        specifybelowradixlabel.pack(pady=15)

        specown=Button(specifyingframe,height=2,width=27,text='Owner Login',bg='#ED7020',fg='white',font=('Orbitron',12),command=loginpage)
        specown.pack(pady=15)

        specadmin=Button(specifyingframe,height=2,width=27,text='Admin Login',bg='#ED7020',fg='white',font=('Orbitron',12),command=admins_login)
        specadmin.pack(pady=15)


        specdoc=Button(specifyingframe,height=2,width=27,text='Doctor Login',bg='#ED7020',fg='white',font=('Orbitron',12),command=doc_prtl)
        specdoc.pack(pady=20)


        backing_button_to_welcome_page=Button(specifyingframe,width=10,pady=7,text='⬅Back',bg='#ED7020',fg='white',border=0,command=back_to_wc)
        backing_button_to_welcome_page.pack()
    
        
    log.geometry('925x600')
    log.resizable(False,False)
    log.title("Redix Health Care System")
    

    pleaseselect=Label(log,text='Welcome to Redix',font=('Drexs',30))
    pleaseselect.pack(ipady=2)


    loginselection=Button(log,height=2,width=34,text='Go to Login Page',bg='#ED7020',fg='white',font=('Orbitron',12),command=specifying)
    loginselection.pack(pady=61)

    othermenus=Button(log,height=2,width=34,text='Other menus',bg='#ED7020',fg='white',font=('Orbitron',12),command=othr_labs)
    othermenus.pack(pady=32)

startingpage()

log.mainloop()