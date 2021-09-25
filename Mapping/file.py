race_mapping= {'Black African':0, 'Coloured': 1, 'White': 2, 'Indian/Asian':3}

dwelling_mapping= {'Dwelling/house or brick/concrete block structure on a separate stand or yard or farm': 0,
                   'Traditional dwelling/hut/structure made of traditional materials': 1, 
                   'Informal dwelling/shack not in backyard, e.g in an informal/squatter settlement or on a farm.':2,
                   'Informal dwelling/shack in backyard': 3, 
                   'Flat or apartment in a block of flats': 4, 
                   'Room/flat let on a property or a larger dwelling/servants quarters/granny flat': 5, 
                   'Dwelling/house/flat/room in backyard': 6, 
                   'Semi-Detached house': 7, 
                   'Town house (semi-detached house in complex)':8, 
                   'Unspecified': 9,
                   'Cluster house in complex': 10,
                   'Other (specify)': 11, 
                   'Caravan/tent':12,
                  }

dwelling_type_mapping= {'Formal': 0, 'Informal':1, 'Unspecified': 2}

province_code_mapping= {'Gauteng':0, 'KwaZulu-Natal':1, 'Eastern Cape': 2, 'Limpopo': 3, 'Western Cape': 4,
                        'Mpumalanga': 5, 'Free State': 6, 'North West':7, 'Northern Cape': 8}

metro_code_mapping= {'KZN - Non Metro':0, 'LP - Non Metro':1, 'EC - Non Metro': 2, 'MP - Non Metro':3, 'GP - City of Johannesburg': 4,
                     'WC - City of Cape Town':5, 'NW - Non Metro': 6, 'GP - Ekurhuleni':7, 'GP - City of Tshwane': 8,
                     'KZN - eThekwini': 9, 'FS - Non Metro': 10, 'NC - Non Metro': 11, 'GP - Non Metro': 12, 'WC - Non Metro': 13,
                     'EC - Nelson Mandela Bay': 14, 'FS - Mangaung': 15, 'EC - Buffalo City': 16}

nationality_mapping= {'South Africa':0, 'Other':1, 'Unspecified': 2}

RTH_mapping= {'Head/acting head':0, 'Husband/wife/partner of person 01':1, 'Son/daughter/stepchild/adopted child of person 01':2,
              'Other relative (e.g. in-laws or aunt/uncle) of person 01': 3, 'Brother/sister/stepbrother/stepsister of person 01': 4,
              'Grandchild/great grandchild of person 01': 5, 'Father/mother/stepfather/stepmother of person 01':6, 'Non-related persons':7,
              'Grandparent/great grandparent of person 01':8, 'Unspecified': 9}

marital_st_mapping={'Single and have never been married/never lived together as husband/wife before': 0, 'Married':1,
                    'Widowed': 2, 'Living together like husband and wife':3, 'Divorced': 4, 'Single; but have been living together with someone as husband/wife before':5,
                    'Separated; but still legally married': 6, 'Unspecified':7}

Lang_inside_mapping= {'IsiZulu':0, 'IsiXhosa': 1, 'Afrikaans': 2, 'Sepedi': 3, 'Sesotho': 4, 'Setswana': 5, 'English': 6,
                      'Xitsonga': 7, 'SiSwati': 8, 'Tshivenda': 9, 'Other (Specify )': 10, 'IsiNdebele': 11, 'Unspecified': 12,
                      'Khoi, Nama and San languages': 13,'Sign language': 14}


Lang_outside_mapping= {'IsiZulu':0, 'IsiXhosa': 1, 'Afrikaans': 2, 'Sepedi': 3, 'Sesotho': 4, 'Setswana': 5, 'English': 6,
                      'Xitsonga': 7, 'SiSwati': 8, 'Tshivenda': 9, 'Other (Specify )': 10, 'IsiNdebele': 11, 'Unspecified': 12,
                      'Khoi, Nama and San languages': 13}

Education_mapping= {'Grade 12/Standard 10/Form 5/Matric (No Exemption)':0, 'Grade 11/Standard 9/Form 4':1, 'Grade 10/Standard 8/Form 3': 2, 'Unspecified': 3,
                    'Grade 9/Standard 7/Form 2/AET 4':4, 'Grade 8/Standard 6/Form 1':5, 'Grade 7/Standard 5/AET 3': 6, 'Diploma with Grade 12/Std 10': 7, 'Grade 6/Standard 4': 8, 
                    'Bachelor�s Degree': 9, 'Grade 4/Standard 2': 10, 'Grade 5/Standard 3/AET 2': 11, 'Certificate with Grade 12/Std 10': 12, 'Grade 3/Standard 1/AET 1 (Kha Ri Gude; Sanli)': 13,
                    'Higher Diploma (Technikon/University of Technology)': 14, 'Grade 12/Standard 10/Form 5/Matric (Exemption *)': 15, 'Grade 2/Sub B/Class 2': 16, 'Honours Degree': 17, 
                    'Do not know': 18, 'Grade 1/Sub A/Class 1': 19, "Higher degree (Master's; Doctorate)": 20, "Post-Higher Diploma (Technikon/University of Technology; Master's; Doctoral)":21,
                    'Other': 22, 'Bachelor�s Degree and post-graduate diploma': 23, 'Diploma with less than Grade 12/Std 10': 24, 'NTC 3/N3/NC (V)/Level 4': 25, 'N6/NTC 6': 26, 'Certificate with less than Grade 12/Std 10': 27,
                    'N5/NTC 5': 28, 'N4/NTC 4': 29, 'NTC 2/N2/NC (V)/Level 3': 30, 'Grade R/0': 31, 'NTC 1/N1/NC (V) /Level 2': 32}

lw_work_mapping= {'No': 0, 'Yes': 1, 'Unspecified': 2, 'Do not know': 3}

lw_business_mapping= {'No': 0, 'Yes': 1, 'Unspecified': 2, 'Do not know': 3}

help_on_household_mapping= {'No': 0, 'Yes': 1, 'Unspecified': 2, 'Do not know': 3}

job_or_business_mapping={'No': 0, 'Not applicable': 1, 'Unspecified': 2, 'Yes': 3, 'Do not know': 4 }

nature_of_work_mapping= {'Not applicable': 0, 'Permanent': 1, 'Temporary': 2, 'A fixed period contract': 3, 'Casual': 4,
                         'Unspecified': 5, 'Seasonal': 6, 'Do not know': 7}

