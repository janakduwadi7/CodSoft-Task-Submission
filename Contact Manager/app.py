from flask import Flask,render_template,jsonify,request

app=Flask(__name__)

contact_info=[{"id":1,"Name":"John Doe","Phone":9812345670,"Email":"john@gmail.com","Address":"Kathmandu,Nepal"},
              {"id":2,"Name":"Harry","Phone":9812345670,"Email":"harry@gmail.com","Address":"Dhading,Nepal"}
              ]

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/api/contact_info',methods=['GET'])
def get_contact_info():
    return jsonify(contact_info)

@app.route('/api/contact_info',methods=['POST'])
def add_contact_info():
    contact_data=request.form
    contact_id=contact_data.get('id',len(contact_info)+1)
    contact_name=contact_data.get('Name')
    contact_phone=contact_data.get('Phone')
    contact_email=contact_data.get('Email')
    contact_address=contact_data.get('Address')
    new_contact={"id":contact_id,"Name":contact_name,"Phone":contact_phone,"Email":contact_email,"Address":contact_address}
    contact_info.append(new_contact)
    return render_template('index.html',contact_info=contact_info)

@app.route('/api/contact_info/<int:contact_id>',methods=['PUT'])
def update_contatc(contact_id):
    data=request.json
    for contact in contact_info:
        if contact['id']==contact_id:
            contact["Name"]=data.get('Name',contact["Name"])
            contact['Phone']=data.get("Phone",contact["Phone"])
            return jsonify({"message":"Contact updated successfully."})
        return jsonify({"message":"Cannot find the contact with that specific name"})

@app.route('/api/contact_info/<int:contact_id>',methods=['DELETE'])
def delete_contact(contact_id):
    global contact_info
    contact_info=[contact for contact in contact_info if contact['id']!=contact_id]
    return jsonify({"message":"Contact Deleted Successfully"})


if __name__=="__main__":
    app.run(debug=True)