def content():
    user_dict = {"Profile": [["Name", "#"], ["Date of Birth", "#"], ["Blood Group", "#"],
                             ["Age", "#"], ["Update Details", "/update/"]],
                 "Home": ["Donate", "Your Contributions", "People"],
                 "Contact": ["sritejakittu777@gmail.com", "chinnicharan14@gmail.com"]}
    return user_dict


def bloodgroups():
    blood_group_list = ["A+", "A-", "B+", "B-", "AB+", "AB-", "A1+", "A1-", "A2+",
                        "A2-", "A1B+", "A1B-", "A2B+", "A2B-", "O+", "O-"]
    bg_list = [('', '---Select blood group---')]
    j = 1
    for i in blood_group_list:
        bg_list.append((i, i))
        j += 1
    return bg_list

def short_bd_list():
    return ['A+', 'A-', 'B-', 'B+', 'AB+', 'AB-', 'O+', 'O-']


def get_states_list():
    return [
        'Assam',
        'Andhra Pradesh',
        'Odisha',
        'Punjab',
        'Delhi',
        'Gujarat',
        'Karnataka',
        'Haryana',
        'Rajasthan',
        'Himachal Pradesh',
        'Uttarakhand',
        'Jharkhand',
        'Chhattisgarh',
        'Kerala',
        'Tamil Nadu',
        'Madhya Pradesh',
        'West Bengal',
        'Bihar',
        'Maharashtra',
        'Uttar Pradesh',
        'Chandigarh',
        'Telangana',
        'Jammu and Kashmir',
        'Tripura',
        'Meghalaya',
        'Goa',
        'Arunachal Pradesh',
        'Manipur',
        'Mizoram',
        'Sikkim',
        'Puducherry',
        'Nagaland',
        'Andaman and Nicobar Islands',
        'Dadra and Nagar Haveli',
        'Daman and Diu',
        'Lakshadweep'
    ]


def state_list():
    states_list = [
        'Andaman and Nicobar Islands',
        'Andhra Pradesh',
        'Arunachal Pradesh',
        'Assam',
        'Bihar',
        'Chandigarh',
        'Chhattisgarh',
        'Dadra and Nagar Haveli',
        'Daman and Diu',
        'Delhi',
        'Goa',
        'Gujarat',
        'Haryana',
        'Himachal Pradesh',
        'Jammu and Kashmir',
        'Jharkhand',
        'Karnataka',
        'Kerala',
        'Lakshadweep',
        'Madhya Pradesh',
        'Maharashtra',
        'Manipur',
        'Meghalaya',
        'Mizoram',
        'Nagaland',
        'Odisha',
        'Puducherry',
        'Punjab',
        'Rajasthan',
        'Sikkim',
        'Tamil Nadu',
        'Telangana',
        'Tripura',
        'Uttar Pradesh',
        'Uttarakhand',
        'West Bengal'
    ]
    states_tuple_list = []
    for i in states_list:
        states_tuple_list.append((i, i))
    states_tuple_list.insert(0, ('', 'Please select your current resident state'))
    return states_tuple_list


def gender_list():
    return [('', '---Please Select Gender---'), ('Male', 'Male'), ('Female', 'Female'),
            ('Other', 'Other'), ('Not known', 'I am not interested to reveal my gender')]


def cities_list():
    cities_dict = {
        'Andaman and Nicobar Islands': ['Port Blair'],
        'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Rajahmundry', 'Kakinada',
                           'Tirupati', 'Anantapur', 'Kadapa', 'Vizianagaram', 'Eluru', 'Ongole', 'Nandyal',
                           'Machilipatnam', 'Adoni', 'Tenali', 'Chittoor', 'Hindupur', 'Proddatur', 'Bhimavaram',
                           'Madanapalle', 'Guntakal', 'Dharmavaram', 'Gudivada', 'Srikakulam', 'Narasaraopet',
                           'Rajampet', 'Tadpatri', 'Tadepalligudem', 'Chilakaluripet', 'Yemmiganur', 'Kadiri',
                           'Chirala', 'Anakapalle', 'Kavali', 'Palacole', 'Sullurpeta', 'Tanuku', 'Rayachoti',
                           'Srikalahasti', 'Bapatla', 'Naidupet', 'Nagari', 'Gudur', 'Vinukonda', 'Narasapuram',
                           'Nuzvid', 'Markapur', 'Ponnur', 'Kandukur', 'Bobbili', 'Rayadurg', 'Samalkot', 'Jaggaiahpet',
                           'Tuni', 'Amalapuram', 'Bheemunipatnam', 'Venkatagiri', 'Sattenapalle', 'Pithapuram',
                           'Palasa Kasibugga', 'Parvathipuram', 'Macherla', 'Gooty', 'Salur', 'Mandapeta',
                           'Jammalamadugu', 'Peddapuram', 'Punganur', 'Nidadavole', 'Repalle', 'Ramachandrapuram',
                           'Kovvur', 'Tiruvuru', 'Uravakonda', 'Narsipatnam', 'Yerraguntla', 'Pedana', 'Puttur',
                           'Renigunta', 'Rajam', 'Srisailam Project (Right Flank Colony) Township'],

        'Arunachal Pradesh': ['Naharlagun', 'Pasighat'],

        'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Nagaon', 'Tinsukia', 'Jorhat', 'Bongaigaon City', 'Dhubri',
                  'Diphu', 'North Lakhimpur', 'Tezpur', 'Karimganj', 'Sibsagar', 'Goalpara', 'Barpeta', 'Lanka',
                  'Lumding', 'Mankachar', 'Nalbari', 'Rangia', 'Margherita', 'Mangaldoi', 'Silapathar', 'Mariani',
                  'Marigaon'],

        'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Darbhanga', 'Arrah', 'Begusarai', 'Chhapra', 'Katihar',
                  'Munger', 'Purnia', 'Saharsa', 'Sasaram', 'Hajipur', 'Dehri-on-Sone', 'Bettiah', 'Motihari', 'Bagaha',
                  'Siwan', 'Kishanganj', 'Jamalpur', 'Buxar', 'Jehanabad', 'Aurangabad', 'Lakhisarai', 'Nawada',
                  'Jamui', 'Sitamarhi', 'Araria', 'Gopalganj', 'Madhubani', 'Masaurhi', 'Samastipur', 'Mokameh',
                  'Supaul', 'Dumraon', 'Arwal', 'Forbesganj', 'BhabUrban Agglomeration', 'Narkatiaganj', 'Naugachhia',
                  'Madhepura', 'Sheikhpura', 'Sultanganj', 'Raxaul Bazar', 'Ramnagar', 'Mahnar Bazar', 'Warisaliganj',
                  'Revelganj', 'Rajgir', 'Sonepur', 'Sherghati', 'Sugauli', 'Makhdumpur', 'Maner', 'Rosera', 'Nokha',
                  'Piro', 'Rafiganj', 'Marhaura', 'Mirganj', 'Lalganj', 'Murliganj', 'Motipur', 'Manihari', 'Sheohar',
                  'Maharajganj', 'Silao', 'Barh', 'Asarganj'],

        'Chandigarh': ['Chandigarh'],

        'Chhattisgarh': ['Raipur', 'Bhilai Nagar', 'Korba', 'Bilaspur', 'Durg', 'Rajnandgaon', 'Jagdalpur', 'Raigarh',
                         'Ambikapur', 'Mahasamund', 'Dhamtari', 'Chirmiri', 'Bhatapara', 'Dalli-Rajhara',
                         'Naila Janjgir', 'Tilda Newra', 'Mungeli', 'Manendragarh', 'Sakti'],

        'Dadra and Nagar Haveli': ['Silvassa'],

        'Daman and Diu': ['Daman', 'Diu'],

        'Delhi': ['Delhi', 'New Delhi'],

        'Goa': ['Marmagao', 'Panaji', 'Margao', 'Mapusa'],

        'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar', 'Jamnagar', 'Nadiad', 'Porbandar', 'Anand',
                    'Morvi', 'Mahesana', 'Bharuch', 'Vapi', 'Navsari', 'Veraval', 'Bhuj', 'Godhra', 'Palanpur',
                    'Valsad', 'Patan', 'Deesa', 'Amreli', 'Anjar', 'Dhoraji', 'Khambhat', 'Mahuva', 'Keshod', 'Wadhwan',
                    'Ankleshwar', 'Savarkundla', 'Kadi', 'Visnagar', 'Upleta', 'Una', 'Sidhpur', 'Unjha', 'Mangrol',
                    'Viramgam', 'Modasa', 'Palitana', 'Petlad', 'Kapadvanj', 'Sihor', 'Wankaner', 'Limbdi', 'Mandvi',
                    'Thangadh', 'Vyara', 'Padra', 'Lunawada', 'Rajpipla', 'Vapi', 'Umreth', 'Sanand', 'Rajula',
                    'Radhanpur', 'Mahemdabad', 'Ranavav', 'Tharad', 'Mansa', 'Umbergaon', 'Talaja', 'Vadnagar',
                    'Manavadar', 'Salaya', 'Vijapur', 'Pardi', 'Rapar', 'Songadh', 'Lathi', 'Adalaj', 'Chhapra'],

        'Haryana': ['Faridabad', 'Gurgaon', 'Hisar', 'Rohtak', 'Panipat', 'Karnal', 'Sonipat', 'Yamunanagar',
                    'Panchkula', 'Bhiwani', 'Bahadurgarh', 'Jind', 'Sirsa', 'Thanesar', 'Kaithal', 'Palwal', 'Rewari',
                    'Hansi', 'Narnaul', 'Fatehabad', 'Gohana', 'Tohana', 'Narwana', 'Mandi Dabwali', 'Charkhi Dadri',
                    'Shahbad', 'Pehowa', 'Samalkha', 'Pinjore', 'Ladwa', 'Sohna', 'Safidon', 'Taraori', 'Mahendragarh',
                    'Ratia', 'Rania', 'Sarsod'],

        'Himachal Pradesh': ['Shimla', 'Mandi', 'Solan', 'Nahan', 'Sundarnagar', 'Palampur'],

        'Jammu and Kashmir': ['Srinagar', 'Jammu', 'Baramula', 'Anantnag', 'Sopore', 'KathUrban Agglomeration',
                              'Rajauri', 'Punch', 'Udhampur'],

        'Jharkhand': ['Dhanbad', 'Ranchi', 'Jamshedpur', 'Bokaro Steel City', 'Deoghar', 'Phusro', 'Adityapur',
                      'Hazaribag', 'Giridih', 'Ramgarh', 'Jhumri Tilaiya', 'Saunda', 'Sahibganj',
                      'Medininagar (Daltonganj)', 'Chaibasa', 'Chatra', 'Gumia', 'Dumka', 'Madhupur', 'Chirkunda',
                      'Pakaur', 'Simdega', 'Musabani', 'Mihijam', 'Patratu', 'Lohardaga', 'Tenu dam-cum-Kathhara'],

        'Karnataka': ['Bengaluru', 'Hubli-Dharwad', 'Belagavi', 'Mangaluru', 'Davanagere', 'Ballari', 'Tumkur',
                      'Shivamogga', 'Raayachuru', 'Robertson Pet', 'Kolar', 'Mandya', 'Udupi', 'Chikkamagaluru',
                      'Karwar', 'Ranebennuru', 'Ranibennur', 'Ramanagaram', 'Gokak', 'Yadgir', 'Rabkavi Banhatti',
                      'Shahabad', 'Sirsi', 'Sindhnur', 'Tiptur', 'Arsikere', 'Nanjangud', 'Sagara', 'Sira', 'Puttur',
                      'Athni', 'Mulbagal', 'Surapura', 'Siruguppa', 'Mudhol', 'Sidlaghatta', 'Shahpur',
                      'Saundatti-Yellamma', 'Wadi', 'Manvi', 'Nelamangala', 'Lakshmeshwar', 'Ramdurg', 'Nargund',
                      'Tarikere', 'Malavalli', 'Savanur', 'Lingsugur', 'Vijayapura', 'Sankeshwara', 'Madikeri',
                      'Talikota', 'Sedam', 'Shikaripur', 'Mahalingapura', 'Mudalagi', 'Muddebihal', 'Pavagada', 'Malur',
                      'Sindhagi', 'Sanduru', 'Afzalpur', 'Maddur', 'Madhugiri', 'Tekkalakote', 'Terdal', 'Mudabidri',
                      'Magadi', 'Navalgund', 'Shiggaon', 'Shrirangapattana', 'Sindagi', 'Sakaleshapura', 'Srinivaspur',
                      'Ron', 'Mundargi', 'Sadalagi', 'Piriyapatna', 'Adyar', 'Mysore'],

        'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Kollam', 'Thrissur', 'Palakkad', 'Alappuzha',
                   'Malappuram', 'Ponnani', 'Vatakara', 'Kanhangad', 'Taliparamba', 'Koyilandy', 'Neyyattinkara',
                   'Kayamkulam', 'Nedumangad', 'Kannur', 'Tirur', 'Kottayam', 'Kasaragod', 'Kunnamkulam', 'Ottappalam',
                   'Thiruvalla', 'Thodupuzha', 'Chalakudy', 'Changanassery', 'Punalur', 'Nilambur', 'Cherthala',
                   'Perinthalmanna', 'Mattannur', 'Shoranur', 'Varkala', 'Paravoor', 'Pathanamthitta', 'Peringathur',
                   'Attingal', 'Kodungallur', 'Pappinisseri', 'Chittur-Thathamangalam', 'Muvattupuzha', 'Adoor',
                   'Mavelikkara', 'Mavoor', 'Perumbavoor', 'Vaikom', 'Palai', 'Panniyannur', 'Guruvayoor',
                   'Puthuppally', 'Panamattom'],

        'Lakshadweep': ['Kavaratti', 'Minicoy'],

        'Madhya Pradesh': ['Indore', 'Bhopal', 'Jabalpur', 'Gwalior', 'Ujjain', 'Sagar', 'Ratlam', 'Satna',
                           'Murwara (Katni)', 'Morena', 'Singrauli', 'Rewa', 'Vidisha', 'Ganjbasoda', 'Shivpuri',
                           'Mandsaur', 'Neemuch', 'Nagda', 'Itarsi', 'Sarni', 'Sehore', 'Mhow Cantonment', 'Seoni',
                           'Balaghat', 'Ashok Nagar', 'Tikamgarh', 'Shahdol', 'Pithampur', 'Alirajpur', 'Mandla',
                           'Sheopur', 'Shajapur', 'Panna', 'Raghogarh-Vijaypur', 'Sendhwa', 'Sidhi', 'Pipariya',
                           'Shujalpur', 'Sironj', 'Pandhurna', 'Nowgong', 'Mandideep', 'Sihora', 'Raisen', 'Lahar',
                           'Maihar', 'Sanawad', 'Sabalgarh', 'Umaria', 'Porsa', 'Narsinghgarh', 'Malaj Khand',
                           'Sarangpur', 'Mundi', 'Nepanagar', 'Pasan', 'Mahidpur', 'Seoni-Malwa', 'Rehli', 'Manawar',
                           'Rahatgarh', 'Panagar', 'Wara Seoni', 'Tarana', 'Sausar', 'Rajgarh', 'Niwari', 'Mauganj',
                           'Manasa', 'Nainpur', 'Prithvipur', 'Sohagpur', 'Nowrozabad (Khodargama)', 'Shamgarh',
                           'Maharajpur', 'Multai', 'Pali', 'Pachore', 'Rau', 'Mhowgaon', 'Vijaypur', 'Narsinghgarh'],

        'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Thane', 'Nashik', 'Kalyan-Dombivali', 'Vasai-Virar', 'Solapur',
                        'Mira-Bhayandar', 'Bhiwandi', 'Amravati', 'Nanded-Waghala', 'Sangli', 'Malegaon', 'Akola',
                        'Latur', 'Dhule', 'Ahmednagar', 'Ichalkaranji', 'Parbhani', 'Panvel', 'Yavatmal', 'Achalpur',
                        'Osmanabad', 'Nandurbar', 'Satara', 'Wardha', 'Udgir', 'Aurangabad', 'Amalner', 'Akot',
                        'Pandharpur', 'Shrirampur', 'Parli', 'Washim', 'Ambejogai', 'Manmad', 'Ratnagiri',
                        'Uran Islampur', 'Pusad', 'Sangamner', 'Shirpur-Warwade', 'Malkapur', 'Wani', 'Lonavla',
                        'Talegaon Dabhade', 'Anjangaon', 'Umred', 'Palghar', 'Shegaon', 'Ozar', 'Phaltan', 'Yevla',
                        'Shahade', 'Vita', 'Umarkhed', 'Warora', 'Pachora', 'Tumsar', 'Manjlegaon', 'Sillod', 'Arvi',
                        'Nandura', 'Vaijapur', 'Wadgaon Road', 'Sailu', 'Murtijapur', 'Tasgaon', 'Mehkar', 'Yawal',
                        'Pulgaon', 'Nilanga', 'Wai', 'Umarga', 'Paithan', 'Rahuri', 'Nawapur', 'Tuljapur', 'Morshi',
                        'Purna', 'Satana', 'Pathri', 'Sinnar', 'Uchgaon', 'Uran', 'Pen', 'Karjat', 'Manwath', 'Partur',
                        'Sangole', 'Mangrulpir', 'Risod', 'Shirur', 'Savner', 'Sasvad', 'Pandharkaoda', 'Talode',
                        'Shrigonda', 'Shirdi', 'Raver', 'Mukhed', 'Rajura', 'Vadgaon Kasba', 'Tirora', 'Mahad', 'Lonar',
                        'Sawantwadi', 'Pathardi', 'Pauni', 'Ramtek', 'Mul', 'Soyagaon', 'Mangalvedhe', 'Narkhed',
                        'Shendurjana', 'Patur', 'Mhaswad', 'Loha', 'Nandgaon', 'Warud'],

        'Manipur': ['Imphal', 'Thoubal', 'Lilong', 'Mayang Imphal'],

        'Meghalaya': ['Shillong', 'Tura', 'Nongstoin'],

        'Mizoram': ['Aizawl', 'Lunglei', 'Saiha'],

        'Nagaland': ['Dimapur', 'Kohima', 'Zunheboto', 'Tuensang', 'Wokha', 'Mokokchung'],

        'Odisha': ['Bhubaneswar', 'Cuttack', 'Raurkela', 'Brahmapur', 'Sambalpur', 'Puri', 'Baleshwar Town',
                   'Baripada Town', 'Bhadrak', 'Balangir', 'Jharsuguda', 'Bargarh', 'Paradip', 'Bhawanipatna',
                   'Dhenkanal', 'Barbil', 'Kendujhar', 'Sunabeda', 'Rayagada', 'Jatani', 'Byasanagar', 'Kendrapara',
                   'Rajagangapur', 'Parlakhemundi', 'Talcher', 'Sundargarh', 'Phulabani', 'Pattamundai', 'Titlagarh',
                   'Nabarangapur', 'Soro', 'Malkangiri', 'Rairangpur', 'Tarbha'],

        'Puducherry': ['Pondicherry', 'Karaikal', 'Yanam', 'Mahe'],

        'Punjab': ['Ludhiana', 'Patiala', 'Amritsar', 'Jalandhar', 'Bathinda', 'Pathankot', 'Hoshiarpur', 'Batala',
                   'Moga', 'Malerkotla', 'Khanna', 'Mohali', 'Barnala', 'Firozpur', 'Phagwara', 'Kapurthala',
                   'Zirakpur', 'Kot Kapura', 'Faridkot', 'Muktsar', 'Rajpura', 'Sangrur', 'Fazilka', 'Gurdaspur',
                   'Kharar', 'Gobindgarh', 'Mansa', 'Malout', 'Nabha', 'Tarn Taran', 'Jagraon', 'Sunam', 'Dhuri',
                   'Firozpur Cantt.', 'Sirhind Fatehgarh Sahib', 'Rupnagar', 'Jalandhar Cantt.', 'Samana', 'Nawanshahr',
                   'Rampura Phul', 'Nangal', 'Nakodar', 'Zira', 'Patti', 'Raikot', 'Longowal', 'Urmar Tanda',
                   'Morinda, India', 'Phillaur', 'Pattran', 'Qadian', 'Sujanpur', 'Mukerian', 'Talwara'],

        'Rajasthan': ['Jaipur', 'Jodhpur', 'Bikaner', 'Udaipur', 'Ajmer', 'Bhilwara', 'Alwar', 'Bharatpur', 'Pali',
                      'Barmer', 'Sikar', 'Tonk', 'Sadulpur', 'Sawai Madhopur', 'Nagaur', 'Makrana', 'Sujangarh',
                      'Sardarshahar', 'Ladnu', 'Ratangarh', 'Nokha', 'Nimbahera', 'Suratgarh', 'Rajsamand',
                      'Lachhmangarh', 'Rajgarh (Churu)', 'Nasirabad', 'Nohar', 'Phalodi', 'Nathdwara', 'Pilani',
                      'Merta City', 'Sojat', 'Neem-Ka-Thana', 'Sirohi', 'Pratapgarh', 'Rawatbhata', 'Sangaria',
                      'Lalsot', 'Pilibanga', 'Pipar City', 'Taranagar', 'Vijainagar, Ajmer', 'Sumerpur', 'Sagwara',
                      'Ramganj Mandi', 'Lakheri', 'Udaipurwati', 'Losal', 'Sri Madhopur', 'Ramngarh', 'Rawatsar',
                      'Rajakhera', 'Shahpura', 'Shahpura', 'Raisinghnagar', 'Malpura', 'Nadbai', 'Sanchore', 'Nagar',
                      'Rajgarh (Alwar)', 'Sheoganj', 'Sadri', 'Todaraisingh', 'Todabhim', 'Reengus', 'Rajaldesar',
                      'Sadulshahar', 'Sambhar', 'Prantij', 'Mount Abu', 'Mangrol', 'Phulera', 'Mandawa', 'Pindwara',
                      'Mandalgarh', 'Takhatgarh'],

        'Sikkim': ['Gangtok', 'Pelling', 'Lachung', 'Lachen', 'Namchi', 'Ravangla'],

        'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem', 'Tirunelveli', 'Tiruppur',
                       'Ranipet', 'Nagercoil', 'Thanjavur', 'Vellore', 'Kancheepuram', 'Erode', 'Tiruvannamalai',
                       'Pollachi', 'Rajapalayam', 'Sivakasi', 'Pudukkottai', 'Neyveli (TS)', 'Nagapattinam',
                       'Viluppuram', 'Tiruchengode', 'Vaniyambadi', 'Theni Allinagaram', 'Udhagamandalam',
                       'Aruppukkottai', 'Paramakudi', 'Arakkonam', 'Virudhachalam', 'Srivilliputhur', 'Tindivanam',
                       'Virudhunagar', 'Karur', 'Valparai', 'Sankarankovil', 'Tenkasi', 'Palani', 'Pattukkottai',
                       'Tirupathur', 'Ramanathapuram', 'Udumalaipettai', 'Gobichettipalayam', 'Thiruvarur',
                       'Thiruvallur', 'Panruti', 'Namakkal', 'Thirumangalam', 'Vikramasingapuram', 'Nellikuppam',
                       'Rasipuram', 'Tiruttani', 'Nandivaram-Guduvancheri', 'Periyakulam', 'Pernampattu', 'Vellakoil',
                       'Sivaganga', 'Vadalur', 'Rameshwaram', 'Tiruvethipuram', 'Perambalur', 'Usilampatti',
                       'Vedaranyam', 'Sathyamangalam', 'Puliyankudi', 'Nanjikottai', 'Thuraiyur', 'Sirkali',
                       'Tiruchendur', 'Periyasemur', 'Sattur', 'Vandavasi', 'Tharamangalam', 'Tirukkoyilur',
                       'Oddanchatram', 'Palladam', 'Vadakkuvalliyur', 'Tirukalukundram', 'Uthamapalayam', 'Surandai',
                       'Sankari', 'Shenkottai', 'Vadipatti', 'Sholingur', 'Tirupathur', 'Manachanallur', 'Viswanatham',
                       'Polur', 'Panagudi', 'Uthiramerur', 'Thiruthuraipoondi', 'Pallapatti', 'Ponneri', 'Lalgudi',
                       'Natham', 'Unnamalaikadai', 'P.N.Patti', 'Tharangambadi', 'Tittakudi', 'Pacode', "O' Valley",
                       'Suriyampalayam', 'Sholavandan', 'Thammampatti', 'Namagiripettai', 'Peravurani', 'Parangipettai',
                       'Pudupattinam', 'Pallikonda', 'Sivagiri', 'Punjaipugalur', 'Padmanabhapuram', 'Thirupuvanam'],

        'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Karimnagar', 'Ramagundam', 'Khammam', 'Mahbubnagar',
                      'Mancherial', 'Adilabad', 'Suryapet', 'Jagtial', 'Miryalaguda', 'Nirmal', 'Kamareddy',
                      'Kothagudem', 'Bodhan', 'Palwancha', 'Mandamarri', 'Koratla', 'Sircilla', 'Tandur', 'Siddipet',
                      'Wanaparthy', 'Kagaznagar', 'Gadwal', 'Sangareddy', 'Bellampalle', 'Bhongir', 'Vikarabad',
                      'Jangaon', 'Bhadrachalam', 'Bhainsa', 'Farooqnagar', 'Medak', 'Narayanpet', 'Sadasivpet',
                      'Yellandu', 'Manuguru', 'Kyathampalle', 'Nagarkurnool'],

        'Tripura': ['Agartala', 'Udaipur', 'Dharmanagar', 'Pratapgarh', 'Kailasahar', 'Belonia', 'Khowai'],

        'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Firozabad', 'Agra', 'Meerut', 'Varanasi', 'Allahabad', 'Amroha',
                          'Moradabad', 'Aligarh', 'Saharanpur', 'Noida', 'Loni', 'Jhansi', 'Shahjahanpur', 'Rampur',
                          'Modinagar', 'Hapur', 'Etawah', 'Sambhal', 'Orai', 'Bahraich', 'Unnao', 'Rae Bareli',
                          'Lakhimpur', 'Sitapur', 'Lalitpur', 'Pilibhit', 'Chandausi', 'Hardoi ', 'Azamgarh', 'Khair',
                          'Sultanpur', 'Tanda', 'Nagina', 'Shamli', 'Najibabad', 'Shikohabad', 'Sikandrabad',
                          'Shahabad, Hardoi', 'Pilkhuwa', 'Renukoot', 'Vrindavan', 'Ujhani', 'Laharpur', 'Tilhar',
                          'Sahaswan', 'Rath', 'Sherkot', 'Kalpi', 'Tundla', 'Sandila', 'Nanpara', 'Sardhana', 'Nehtaur',
                          'Seohara', 'Padrauna', 'Mathura', 'Thakurdwara', 'Nawabganj', 'Siana', 'Noorpur',
                          'Sikandra Rao', 'Puranpur', 'Rudauli', 'Thana Bhawan', 'Palia Kalan', 'Zaidpur', 'Nautanwa',
                          'Zamania', 'Shikarpur, Bulandshahr', 'Naugawan Sadat', 'Fatehpur Sikri', 'Shahabad, Rampur',
                          'Robertsganj', 'Utraula', 'Sadabad', 'Rasra', 'Lar', 'Lal Gopalganj Nindaura', 'Sirsaganj',
                          'Pihani', 'Shamsabad, Agra', 'Rudrapur', 'Soron', 'SUrban Agglomerationr', 'Samdhan',
                          'Sahjanwa', 'Rampur Maniharan', 'Sumerpur', 'Shahganj', 'Tulsipur', 'Tirwaganj',
                          'PurqUrban Agglomerationzi', 'Shamsabad, Farrukhabad', 'Warhapur', 'Powayan', 'Sandi',
                          'Achhnera', 'Naraura', 'Nakur', 'Sahaspur', 'Safipur', 'Reoti', 'Sikanderpur', 'Saidpur',
                          'Sirsi', 'Purwa', 'Parasi', 'Lalganj', 'Phulpur', 'Shishgarh', 'Sahawar', 'Samthar',
                          'Pukhrayan', 'Obra', 'Niwai'],

        'Uttarakhand': ['Dehradun', 'Hardwar', 'Haldwani-cum-Kathgodam', 'Srinagar', 'Kashipur', 'Roorkee', 'Rudrapur',
                        'Rishikesh', 'Ramnagar', 'Pithoragarh', 'Manglaur', 'Nainital', 'Mussoorie', 'Tehri', 'Pauri',
                        'Nagla', 'Sitarganj', 'Bageshwar'],

        'West Bengal': ['Kolkata', 'Siliguri', 'Asansol', 'Raghunathganj', 'Kharagpur', 'Naihati', 'English Bazar',
                        'Baharampur', 'Hugli-Chinsurah', 'Raiganj', 'Jalpaiguri', 'Santipur', 'Balurghat', 'Medinipur',
                        'Habra', 'Ranaghat', 'Bankura', 'Nabadwip', 'Darjiling', 'Purulia', 'Arambagh', 'Tamluk',
                        'AlipurdUrban Agglomerationr', 'Suri', 'Jhargram', 'Gangarampur', 'Rampurhat', 'Kalimpong',
                        'Sainthia', 'Taki', 'Murshidabad', 'Memari', 'Paschim Punropara', 'Tarakeswar', 'Sonamukhi',
                        'PandUrban Agglomeration', 'Mainaguri', 'Malda', 'Panchla', 'Raghunathpur', 'Mathabhanga',
                        'Monoharpur', 'Srirampore', 'Adra']
    }

    return cities_dict


def who_can_donate():
    receive_dict = {
        'O+': ['O+', 'O-'],
        'A+': ['A+', 'A-', 'O+','O-'],
        'B+': ['B+', 'B-', 'O+', 'O-'],
        'AB+': ["A+", "A-", "B+", "B-", "AB+", "AB-", "A1+", "A1-", "A2+",
                "A2-", "A1B+", "A1B-", "A2B+", "A2B-", "O+", "O-"],
        'O-': ['O-'],
        'A-': ['A-', 'O-'],
        'B-': ['B-', 'O-'],
        'AB-': ['AB-', 'A-', 'B-', 'O-'],
        'A1+': ['A1+'],
        'A1-': ['A1-'],
        'A2+': ['A2+'],
        'A2-': ['A2-'],
        'A1B+': ['A1B+'],
        'A2B+': ['A2B+'],
        'A2B-': ['A2B-']
    }
    return receive_dict