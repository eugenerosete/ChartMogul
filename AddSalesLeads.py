import chartmogul

def AddSalesLead(emailList, salesLead):
    for memberEmail in emailList:
        msg = chartmogul.CustomAttributes.add(
            config,
            data={
                'email': memberEmail, 
                'custom': [
                    {"type": "String", "key": "Sales Lead", "value": salesLead}
                ]
            }
        )

        print(msg, end="\n\n")

config = chartmogul.Config('0bf0c27f6492ce2ce8d88c5ca9ea6bba', '7fa2c0e0515d1b916997a42db98fd675')

MaknaeLine = ["giraffe@runningman.com", "yangsechan@runningman.com", "jeonsomin@runningman.com"]
InfiniteLine = ["yujaeseok@runningman.com", "haha@runningman.com"]
OustLine = ["kimjongkuk@runningman.com", "jiseokjin@runningman.com", "songjihyo@runningman.com"]
PastLine = ["kanggary@runningman.com", "songjoongki@runningman.com"]

AddSalesLead(MaknaeLine, "Tim Cook")
AddSalesLead(InfiniteLine, "Bill Gates")
AddSalesLead(OustLine, "Steve Jobs")
AddSalesLead(PastLine, "Larry Ellison")
