
# coding: utf-8

# In[1]:


#Form that accepts contact information: first name, last name, age, email address, phone number


# In[2]:


def all_clear(validation):
    #print(validation)
    state = True
    for v in validation.values():
        if v != 'pass':
            state = False
    return state


# In[3]:


import datetime
def get_field(prompt="Enter value: ", required=False, datatype="string"):
    validation = {'required':'fail', 'datatype':'fail'}
    while not all_clear(validation):
        print(prompt, flush=True)
        value = input()
        if not required:
            validation['required'] = 'pass'
        else:
            if len(value) > 0:
                validation['required'] = 'pass'
            else:
                print('Value cannot be missing', flush=False)
        if datatype == 'string':
            validation['datatype'] = 'pass'
        elif datatype == 'numeric':
            try:
                value = float(value)
                validation['datatype'] = 'pass'
            except:
                validation['datatype'] = 'fail'
                print('Please enter a number', flush=False)
        elif datatype == 'datetime':
            try:
                check = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
                validation['datatype'] = 'pass'
            except:
                validation['datatype'] = 'fail'
                print('Please enter a valid date in the format yyyy-mm-ddThh:mm:ss (eg. 2018-07-06T18:16:23)', flush=False)
    return value


# In[4]:


contact_info_schema = """field_name,prompt,required,datatype
first_name,Enter your first name,1,string
age,Enter your age,1,numeric
timestamp,Timestamp (eg. 2018-07-06T18:16:23): ,1,datetime"""


# In[5]:


def run_form(schema):
    output = {}
    import io, csv
    with io.StringIO(schema) as f:
        reader = csv.DictReader(f)
        for row in reader:
            #print(row)
            output[row['field_name']] = get_field(prompt=row['prompt'], required=row['required']=='1', datatype=row['datatype'])
    return output


# In[6]:


contact_info = run_form(contact_info_schema)


# In[7]:


#contact_info['first_name'] = get_field("First name: ", required=True, datatype="string")
#contact_info['age'] = get_field("Age: ", required=True, datatype="numeric")
#contact_info['timestamp'] = get_field("Timestamp: ", required=True, datatype="datetime")


# In[8]:


import json
print(json.dumps(contact_info), flush=True)


# In[ ]:


#Start the server
#!websocketd --port=8080 python chat.py

