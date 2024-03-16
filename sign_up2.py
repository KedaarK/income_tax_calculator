import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from datetime import date
import re
from PIL import ImageTk
import pymysql


def create_sign_up_window():
    def clear():
        first_name_entry.delete(0,END)
        middle_name_entry.delete(0,END)
        last_name_entry.delete(0,END)
        mother_name_entry.delete(0,END)
        dob_entry.delete(0,END)
        age_entry.delete(0,END)
        gender_combobox.delete(0,END)
        mobile_entry.delete(0,END)
        gmail_entry.delete(0,END)
        state_combobox.delete(0,END)
        district_combobox.delete(0,END)
        city_entry.delete(0,END)
        society_street_entry.delete(0,END)
        password_entry.delete(0,END)

    def connect_database():
        try:
            con = pymysql.connect(host='localhost', user='root', password='falked01')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Error')
            return
        try:
            query='create database kedaark5'
            mycursor.execute(query)
            query='use kedaark5'
            mycursor.execute(query)
            query='create table data(Fname varchar(15) not null,Midname varchar(15), Lname varchar(15),Mothername varchar(15),Dob date,age int, gender varchar(10) not null,mobileno varchar(12) not null, gmail varchar(50) primary key not null, State varchar(25) not null, district varchar(25) not null,city varchar(10),society varchar(20), password varchar(10) not null)'
            mycursor.execute(query)
        except:
            mycursor.execute('use kedaark5')

        query='select * from data where gamil = %s'
        mycursor.execute(query,(gmail_entry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'User gmail Already exists')

        else:
            query='insert into data(Fname, Midname, Lname, Mothername, Dob, age, gender, mobileno, gmail,State,district,city,society,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(first_name_entry.get(),middle_name_entry.get(),last_name_entry.get(),mother_name_entry.get(),dob_entry.get(),age_entry.get(),gender_combobox.get(),mobile_entry.get(),gmail_entry.get(),state_combobox.get(),district_combobox.get(),city_entry.get(),society_street_entry.get(),password_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()

    def validate_mobile_number(mobile_number):
        if re.match(r"^\d{10}$", mobile_number):
            return True
        else:
            return False

    # Function to validate Gmail
    def validate_gmail(gmail):
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", gmail):
            return True
        else:
            return False

    def calculate_age(dob):
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def calculate_and_display_age(event):
        dob_str = dob_entry.get()
        try:
            dob = date.fromisoformat(dob_str)
        except ValueError:
            return

        age = calculate_age(dob)

        age_entry.config(state='normal')  # Set the entry state to normal
        age_entry.delete(0, tk.END)
        age_entry.insert(0, age)
        age_entry.config(state='readonly')  # Set the entry state back

    def submit():
        first_name = first_name_entry.get()
        middle_name = middle_name_entry.get()
        last_name = last_name_entry.get()
        mother_name = mother_name_entry.get()
        dob_str = dob_entry.get()
        try:
            dob = date.fromisoformat(dob_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD")
            return

        gender = gender_combobox.get()
        mobile_number = mobile_entry.get()
        gmail = gmail_entry.get()
        state = state_combobox.get()
        district = district_combobox.get()
        city = city_entry.get()
        society_street = society_street_entry.get()  # Get society and street combined
        password = password_entry.get()
        age = calculate_age(dob)

        # Check if any entry is empty
        if not all([first_name, middle_name, last_name, mother_name, dob_str, gender, mobile_number,
                    gmail, state, district, city, society_street]):
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        if not validate_mobile_number(mobile_number):
            messagebox.showerror("Error", "Invalid mobile number")
            return

        if not validate_gmail(gmail):
            messagebox.showerror("Error", "Invalid Gmail")
            return

        age_entry.config(state='normal')  # Set the entry state to normal
        age_entry.delete(0, tk.END)
        age_entry.insert(0, age)
        age_entry.config(state='readonly')  # Set the entry state back to readonly

        print("First Name:", first_name)
        print("Middle Name:", middle_name)
        print("Last Name:", last_name)
        print("Mother's Name:", mother_name)
        print("DOB:", dob)
        print("Age:", age)
        print("Gender:", gender)
        print("Mobile Number:", mobile_number)
        print("Gmail:", gmail)
        print("State:", state)
        print("District:", district)
        print("City:", city)
        print("Society and Street:", society_street)  # Print combined society and street
        print("Password:", password)

        # Show messagebox indicating account creation
        messagebox.showinfo("Success", "Your account has been created successfully!")

        # Close the sign-in window
        root.destroy()

    root = tk.Tk()
    root.title("Sign In Page")
    root.geometry("600x550")  # Increase the size of the window
    root.configure(bg="#fdc1d0")

    label_frame = ttk.LabelFrame(root, text="User Information")  # Change background color as needed
    label_frame.pack(padx=20, pady=20, fill='none', expand=True)

    # Manually define all states and their corresponding districts
    state_districts = {
        "Andhra Pradesh": ["Anantapur", "Chittoor", "East Godavari","Guntur", "Kadapa", "Krishna", "Kurnool",
                           "Nellore", "Prakasam", "Srikakulam", "Visakhapatnam", "Vizianagaram", "West Godavari"],
        "Arunachal Pradesh": ["Tawang", "West Kameng", "East Kameng", "Papum Pare", "Kurung Kumey", "Kra Daadi",
                              "Lower Subansiri", "Upper Subansiri", "West Siang", "East Siang", "Siang", "Upper Siang",
                              "Lower Siang", "Lower Dibang Valley", "Dibang Valley", "Anjaw", "Lohit", "Namsai",
                              "Changlang", "Tirap", "Longding"],
        "Assam": ["Baksa", "Barpeta", "Biswanath", "Bongaigaon", "Cachar", "Charaideo", "Chirang", "Darrang",
                  "Dhemaji", "Dhubri", "Dibrugarh", "Goalpara", "Golaghat", "Hailakandi", "Hojai", "Jorhat", "Kamrup",
                  "Kamrup Metropolitan", "Karbi Anglong", "Karimganj", "Kokrajhar", "Lakhimpur", "Majuli", "Morigaon",
                  "Nagaon", "Nalbari", "Dima Hasao", "Sivasagar", "Sonitpur", "South Salmara-Mankachar", "Tinsukia",
                  "Udalguri", "West Karbi Anglong"],
        "Bihar": ["Araria", "Arwal", "Aurangabad", "Banka", "Begusarai", "Bhagalpur", "Bhojpur", "Buxar", "Darbhanga",
                  "East Champaran (Motihari)", "Gaya", "Gopalganj", "Jamui", "Jehanabad", "Kaimur (Bhabua)", "Katihar",
                  "Khagaria", "Kishanganj", "Lakhisarai", "Madhepura", "Madhubani", "Munger (Monghyr)", "Muzaffarpur",
                  "Nalanda", "Nawada", "Patna", "Purnia (Purnea)", "Rohtas", "Saharsa", "Samastipur", "Saran", "Sheikhpura",
                  "Sheohar", "Sitamarhi", "Siwan", "Supaul", "Vaishali", "West Champaran"],
        "Chhattisgarh": ["Balod", "Baloda Bazar", "Balrampur", "Bastar", "Bemetara", "Bijapur", "Bilaspur", "Dantewada",
                         "Dhamtari", "Durg", "Gariaband", "Janjgir-Champa", "Jashpur", "Kabirdham (Kawardha)", "Kanker (North Bastar)",
                         "Kondagaon", "Korba", "Korea (Koriya)", "Mahasamund", "Mungeli", "Narayanpur", "Raigarh", "Raipur",
                         "Rajnandgaon", "Sukma", "Surajpur", "Surguja"],
        "Goa": ["North Goa", "South Goa"],
        "Gujarat": ["Ahmedabad", "Amreli", "Anand", "Aravalli", "Banaskantha (Palanpur)", "Bharuch", "Bhavnagar", "Botad",
                    "Chhota Udepur", "Dahod", "Dang (Ahwa)", "Devbhoomi Dwarka", "Gandhinagar", "Gir Somnath", "Jamnagar",
                    "Junagadh", "Kachchh", "Kheda (Nadiad)", "Mahisagar", "Mehsana", "Morbi", "Narmada (Rajpipla)", "Navsari",
                    "Panchmahal (Godhra)", "Patan", "Porbandar", "Rajkot", "Sabarkantha (Himmatnagar)", "Surat", "Surendranagar",
                    "Tapi (Vyara)", "Vadodara", "Valsad"],
        "Haryana": ["Ambala", "Bhiwani", "Charkhi Dadri", "Faridabad", "Fatehabad", "Gurugram (Gurgaon)", "Hisar", "Jhajjar",
                    "Jind", "Kaithal", "Karnal", "Kurukshetra", "Mahendragarh", "Nuh", "Palwal", "Panchkula", "Panipat",
                    "Rewari", "Rohtak", "Sirsa", "Sonipat", "Yamunanagar"],
        "Himachal Pradesh": ["Bilaspur", "Chamba", "Hamirpur", "Kangra", "Kinnaur", "Kullu", "Lahaul & Spiti", "Mandi",
                             "Shimla", "Sirmaur (Sirmour)", "Solan", "Una"],
        "Jharkhand": ["Bokaro", "Chatra", "Deoghar", "Dhanbad", "Dumka", "East Singhbhum", "Garhwa", "Giridih", "Godda",
                       "Gumla", "Hazaribag", "Jamtara", "Khunti", "Koderma", "Latehar", "Lohardaga", "Pakur", "Palamu",
                       "Ramgarh", "Ranchi", "Sahibganj", "Seraikela-Kharsawan", "Simdega", "West Singhbhum"],
        "Karnataka": ["Bagalkot", "Ballari (Bellary)", "Belagavi (Belgaum)", "Bengaluru (Bangalore) Rural",
                      "Bengaluru (Bangalore) Urban", "Bidar", "Chamarajanagar", "Chikballapur", "Chikkamagaluru (Chikmagalur)",
                      "Chitradurga", "Dakshina Kannada", "Davangere", "Dharwad", "Gadag", "Hassan", "Haveri", "Kalaburagi (Gulbarga)",
                      "Kodagu", "Kolar", "Koppal", "Mandya", "Mysuru (Mysore)", "Raichur", "Ramanagara", "Shivamogga (Shimoga)",
                      "Tumakuru (Tumkur)", "Udupi", "Uttara Kannada (Karwar)", "Vijayapura (Bijapur)", "Yadgir"],
        "Kerala": ["Alappuzha", "Ernakulam", "Idukki", "Kannur", "Kasaragod", "Kollam", "Kottayam", "Kozhikode", "Malappuram",
                    "Palakkad", "Pathanamthitta", "Thiruvananthapuram", "Thrissur", "Wayanad"],
        "Madhya Pradesh": ["Agar Malwa", "Alirajpur", "Anuppur", "Ashoknagar", "Balaghat", "Barwani", "Betul", "Bhind",
                            "Bhopal", "Burhanpur", "Chhatarpur", "Chhindwara", "Damoh", "Datia", "Dewas", "Dhar", "Dindori",
                            "Guna", "Gwalior", "Harda", "Hoshangabad", "Indore", "Jabalpur", "Jhabua", "Katni", "Khandwa",
                            "Khargone", "Mandla", "Mandsaur", "Morena", "Narsinghpur", "Neemuch", "Panna", "Raisen", "Rajgarh",
                            "Ratlam", "Rewa", "Sagar", "Satna", "Sehore", "Seoni", "Shahdol", "Shajapur", "Sheopur", "Shivpuri",
                            "Sidhi", "Singrauli", "Tikamgarh", "Ujjain", "Umaria", "Vidisha"],
        "Maharashtra": ["Ahmednagar", "Akola", "Amravati", "Aurangabad", "Beed", "Bhandara", "Buldhana", "Chandrapur", "Dhule",
                         "Gadchiroli", "Gondia", "Hingoli", "Jalgaon", "Jalna", "Kolhapur", "Latur", "Mumbai City", "Mumbai Suburban",
                         "Nagpur", "Nanded", "Nandurbar", "Nashik", "Osmanabad", "Palghar", "Parbhani", "Pune", "Raigad", "Ratnagiri",
                         "Sangli", "Satara", "Sindhudurg", "Solapur", "Thane", "Wardha", "Washim", "Yavatmal"],
        "Manipur": ["Bishnupur", "Chandel", "Churachandpur", "Imphal East", "Imphal West", "Jiribam", "Kakching", "Kamjong",
                     "Kangpokpi", "Noney", "Pherzawl", "Senapati", "Tamenglong", "Tengnoupal", "Thoubal", "Ukhrul"],
        "Meghalaya": ["East Garo Hills", "East Jaintia Hills", "East Khasi Hills", "North Garo Hills", "Ri Bhoi", "South Garo Hills",
                        "South West Garo Hills", "South West Khasi Hills", "West Garo Hills", "West Jaintia Hills", "West Khasi Hills"],
        "Mizoram": ["Aizawl", "Champhai", "Hnahthial", "Khawzawl", "Lawngtlai", "Lunglei", "Mamit", "Saiha", "Saitual", "Serchhip"],
        "Nagaland": ["Dimapur", "Kiphire", "Kohima", "Longleng", "Mokokchung", "Mon", "Peren", "Phek", "Tuensang", "Wokha", "Zunheboto"],
        "Odisha": ["Angul", "Balangir", "Balasore", "Bargarh", "Bhadrak", "Boudh", "Cuttack", "Deogarh", "Dhenkanal", "Gajapati",
                   "Ganjam", "Jagatsinghapur", "Jajpur", "Jharsuguda", "Kalahandi", "Kandhamal", "Kendrapara", "Kendujhar (Keonjhar)",
                   "Khordha", "Koraput", "Malkangiri", "Mayurbhanj", "Nabarangpur", "Nayagarh", "Nuapada", "Puri", "Rayagada",
                   "Sambalpur", "Subarnapur (Sonepur)", "Sundargarh"],
        "Punjab": ["Amritsar", "Barnala", "Bathinda", "Faridkot", "Fatehgarh Sahib", "Fazilka", "Ferozepur", "Gurdaspur",
                   "Hoshiarpur", "Jalandhar", "Kapurthala", "Ludhiana", "Mansa", "Moga", "Muktsar", "Nawanshahr (Shahid Bhagat Singh Nagar)",
                   "Pathankot", "Patiala", "Rupnagar", "Sahibzada Ajit Singh Nagar (Mohali)", "Sangrur", "Tarn Taran"],
        "Rajasthan": ["Ajmer", "Alwar", "Banswara", "Baran", "Barmer", "Bharatpur", "Bhilwara", "Bikaner", "Bundi", "Chittorgarh",
                      "Churu", "Dausa", "Dholpur", "Dungarpur", "Hanumangarh", "Jaipur", "Jaisalmer", "Jalore", "Jhalawar",
                      "Jhunjhunu", "Jodhpur", "Karauli", "Kota", "Nagaur", "Pali", "Pratapgarh", "Rajsamand", "Sawai Madhopur",
                      "Sikar", "Sirohi", "Sri Ganganagar", "Tonk", "Udaipur"],
        "Sikkim": ["East Sikkim", "North Sikkim", "South Sikkim", "West Sikkim"],
        "Tamil Nadu": ["Ariyalur", "Chengalpattu", "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode",
                       "Kallakurichi", "Kancheepuram", "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Mayiladuthurai",
                       "Nagapattinam", "Namakkal", "Nilgiris", "Perambalur", "Pudukkottai", "Ramanathapuram", "Ranipet", "Salem",
                       "Sivaganga", "Tenkasi", "Thanjavur", "Theni", "Thoothukudi", "Tiruchirappalli", "Tirunelveli", "Tirupathur",
                       "Tiruppur", "Tiruvallur", "Tiruvannamalai", "Tiruvarur", "Vellore", "Viluppuram", "Virudhunagar"],
        "Telangana": ["Adilabad", "Bhadradri Kothagudem", "Hyderabad", "Jagtial", "Jangaon", "Jayashankar Bhupalapally",
                       "Jogulamba Gadwal", "Kamareddy", "Karimnagar", "Khammam", "Komaram Bheem", "Mahabubabad", "Mahabubnagar",
                       "Mancherial", "Medak", "Medchal", "Mulugu", "Nagarkurnool", "Nalgonda", "Narayanpet", "Nirmal", "Nizamabad",
                       "Peddapalli", "Rajanna Sircilla", "Rangareddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad",
                       "Wanaparthy", "Warangal Rural", "Warangal Urban", "Yadadri Bhuvanagiri"],
        "Tripura": ["Dhalai", "Gomati", "Khowai", "North Tripura", "Sepahijala", "South Tripura", "Unakoti", "West Tripura"],
        "Uttar Pradesh": ["Agra", "Aligarh", "Ambedkar Nagar", "Amethi (Chatrapati Sahuji Mahraj Nagar)", "Amroha (J.P. Nagar)",
                           "Auraiya", "Azamgarh", "Baghpat", "Bahraich", "Ballia", "Balrampur", "Banda", "Barabanki", "Bareilly",
                           "Basti", "Bhadohi", "Bijnor", "Budaun", "Bulandshahr", "Chandauli", "Chitrakoot", "Deoria", "Etah",
                           "Etawah", "Ayodhya (Faizabad)", "Farrukhabad", "Fatehpur", "Firozabad", "Gautam Buddha Nagar",
                           "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hamirpur", "Hapur (Panchsheel Nagar)", "Hardoi", "Hathras",
                           "Jalaun", "Jaunpur", "Jhansi", "Kannauj", "Kanpur Dehat", "Kanpur Nagar", "Kasganj", "Kaushambi", "Kushinagar (Padrauna)",
                           "Lakhimpur - Kheri", "Lalitpur", "Lucknow", "Maharajganj", "Mahoba", "Mainpuri", "Mathura", "Mau", "Meerut",
                           "Mirzapur", "Moradabad", "Muzaffarnagar", "Pilibhit", "Pratapgarh", "Prayagraj", "Raebareli", "Rampur",
                           "Saharanpur", "Sambhal (Bhim Nagar)", "Sant Kabir Nagar", "Shahjahanpur", "Shamali (Prabuddh Nagar)",
                           "Shravasti", "Siddharth Nagar", "Sitapur", "Sonbhadra", "Sultanpur", "Unnao", "Varanasi"],
        "Uttarakhand": ["Almora", "Bageshwar", "Chamoli", "Champawat", "Dehradun", "Haridwar", "Nainital", "Pauri Garhwal",
                          "Pithoragarh", "Rudraprayag", "Tehri Garhwal", "Udham Singh Nagar", "Uttarkashi"],
        "West Bengal": ["Alipurduar", "Bankura", "Birbhum", "Cooch Behar", "Dakshin Dinajpur (South Dinajpur)", "Darjeeling",
                         "Hooghly", "Howrah", "Jalpaiguri", "Jhargram", "Kalimpong", "Kolkata", "Malda", "Murshidabad", "Nadia",
                         "North 24 Parganas", "Paschim Medinipur (West Medinipur)", "Paschim (West) Burdwan (Bardhaman)",
                         "Purba Burdwan (Bardhaman)", "Purba Medinipur (East Medinipur)", "Purulia", "South 24 Parganas",
                         "Uttar Dinajpur (North Dinajpur)"]
    }

    state_label = ttk.Label(label_frame, text="State:")
    state_label.grid(row=9, column=0, padx=5, pady=5)
    state_combobox = ttk.Combobox(label_frame, values=list(state_districts.keys()))
    state_combobox.grid(row=9, column=1, padx=5, pady=5)

    district_label = ttk.Label(label_frame, text="District:")
    district_label.grid(row=10, column=0, padx=5, pady=5)
    district_combobox = ttk.Combobox(label_frame)
    district_combobox.grid(row=10, column=1, padx=5, pady=5)

    def update_districts(event):
        selected_state = state_combobox.get()
        districts = state_districts.get(selected_state, [])
        district_combobox.config(values=districts)

    state_combobox.bind("<<ComboboxSelected>>", update_districts)

    first_name_label = ttk.Label(label_frame, text="First Name:")
    first_name_label.grid(row=0, column=0, padx=5, pady=5)
    first_name_entry = ttk.Entry(label_frame)
    first_name_entry.grid(row=0, column=1, padx=5, pady=5)

    middle_name_label = ttk.Label(label_frame, text="Middle Name:")
    middle_name_label.grid(row=1, column=0, padx=5, pady=5)
    middle_name_entry = ttk.Entry(label_frame)
    middle_name_entry.grid(row=1, column=1, padx=5, pady=5)

    last_name_label = ttk.Label(label_frame, text="Last Name:")
    last_name_label.grid(row=2, column=0, padx=5, pady=5)
    last_name_entry = ttk.Entry(label_frame)
    last_name_entry.grid(row=2, column=1, padx=5, pady=5)

    mother_name_label = ttk.Label(label_frame, text="Mother's Name:")
    mother_name_label.grid(row=3, column=0, padx=5, pady=5)
    mother_name_entry = ttk.Entry(label_frame)
    mother_name_entry.grid(row=3, column=1, padx=5, pady=5)

    dob_label = ttk.Label(label_frame, text="Date of Birth (YYYY-MM-DD):")
    dob_label.grid(row=4, column=0, padx=5, pady=5)
    dob_entry = ttk.Entry(label_frame)
    dob_entry.grid(row=4, column=1, padx=5, pady=5)

    gender_label = ttk.Label(label_frame, text="Gender:")
    gender_label.grid(row=6, column=0, padx=5, pady=5)
    gender_combobox = ttk.Combobox(label_frame, values=["Male", "Female", "Other"])
    gender_combobox.grid(row=6, column=1, padx=5, pady=5)

    mobile_label = ttk.Label(label_frame, text="Mobile Number:")
    mobile_label.grid(row=7, column=0, padx=5, pady=5)
    mobile_entry = ttk.Entry(label_frame)
    mobile_entry.grid(row=7, column=1, padx=5, pady=5)

    gmail_label = ttk.Label(label_frame, text="Gmail:")
    gmail_label.grid(row=8, column=0, padx=5, pady=5)
    gmail_entry = ttk.Entry(label_frame)
    gmail_entry.grid(row=8, column=1, padx=5, pady=5)

    city_label = ttk.Label(label_frame, text="City:")
    city_label.grid(row=11, column=0, padx=5, pady=5)
    city_entry = ttk.Entry(label_frame)
    city_entry.grid(row=11, column=1, padx=5, pady=5)

    society_street_label = ttk.Label(label_frame, text="Society and Street:")
    society_street_label.grid(row=12, column=0, padx=5, pady=5)
    society_street_entry = ttk.Entry(label_frame)
    society_street_entry.grid(row=12, column=1, padx=5, pady=5)

    age_label = ttk.Label(label_frame, text="Age:")
    age_label.grid(row=5, column=0, padx=5, pady=5)
    age_entry = ttk.Entry(label_frame, state='readonly')
    age_entry.grid(row=5, column=1, padx=5, pady=5)

    #password_visible = False

    def toggle_password_visibility():
        global password_visible
        password_visible = False
        if password_visible:
            password_entry.config(show="*")
            password_visible = False
            show_password_button.config(text="Show")
        else:
            password_entry.config(show="")
            password_visible = True
            show_password_button.config(text="Hide")

    password_label = ttk.Label(label_frame, text="Create Password:")
    password_label.grid(row=13, column=0, padx=5, pady=5)
    password_entry = ttk.Entry(label_frame, show="*")
    password_entry.grid(row=13, column=1, padx=10, pady=5, sticky="w")

    show_password_button = ttk.Button(label_frame, text="Show", command=toggle_password_visibility)
    show_password_button.grid(row=13, column=2, padx=10, pady=5, sticky="w")

    dob_entry.bind("<FocusOut>", calculate_and_display_age)

    submit_button = ttk.Button(root, text="Submit", command=lambda: (submit(), connect_database()), style='Custom.TButton')
    submit_button.pack()

    # Define a custom style for the button
    style = ttk.Style()
    style.configure('Custom.TButton', foreground='black',
                    background='#4CAF50', justify='center')  # Change foreground and background colors as needed

    root.mainloop()

#create_sign_up_window()
