import db_helper
def main():
  run=1
  db_helper.create_table()
  while run:
      print("1.insert the value\n2.printing the value\n3.deleting the value \n4.exit")
      choice=input("enter u r choice : ")
      if choice=="1":
        task=str(input("enter the todo: \n"))
        db_helper.data_entry(task)
      elif choice=="2":
        db_helper.printData()
      elif choice=="3":
        userid = str(input("enter the todo's userid to be deleted: \n"))
        db_helper.deleteTask(userid)
      elif choice=="4":
        run=0
      else:
        print("enter the valid choice")

  db_helper.closeCursor()

if __name__ == '__main__': main()

