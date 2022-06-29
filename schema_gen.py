from fileinput import filename
from operator import concat
from tkinter import N


name = input('enter name of your schema:')
file_name = concat(name,'.js')
with open(file_name,'a') as file:
    boilerplate1 = "const mongoose = require('mongoose') \nconst Schema = mongoose.Schema \nconst {}Schema = new Schema(*Define Your Schema*) \n".format(name)
    boilerplate2 = "const {} = mongoose.model('{}', {}Schema) \n".format(name,name,name)
    boilerplate3 = "module.exports = {} \n".format(name)
    file.write(boilerplate1)
    file.write(boilerplate2)
    file.write(boilerplate3)