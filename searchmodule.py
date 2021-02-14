def searching(mylist):
    insights = mylist
    #insights = ["tell","cricket", "stadium"]
    
    game = ["game","centre","gaming","gamer","games","gam"] #0
    library = ["lib","library","libraries","books","book","sit","sitting area","area","libs"] #1
    infrastruture = ["infra","buildings","building","build","built","many","height","block","blocks"] #2
    field = ["ground","field","cricket","stadium","stadiums", "courts" , " basketball", "infrastruture"] #3
    incubation = ["incubation", "incube" , "incub" , "centre","center" , "benifits","benifit" , "special"] #4
    swimpool = ["swim", "swimming","pool" , "pools","water" , "backstroke"] #5
    edubuddy = ['edubuddy',"education","edubuddi" ,'lecture',"lectur","googl", 'download','help','lectures','iiitd','classroom','google', 'syllabus','course'] #6

    checklist = [ game , library, infrastruture , field , incubation, swimpool,edubuddy]

    matches = [0,0,0,0,0,0,0]
    for u in insights:
        for j in checklist:
            for k in j:
                if u == k:
                    matches[checklist.index(j)] += 1
                    break
        
    index_max = max(range(len(matches)), key=matches.__getitem__)

    match_percentage = matches[index_max]/len(insights)
    if(match_percentage >=0.5):
        return index_max
