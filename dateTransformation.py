#Transform date deleting T and Z
def dateModificated(date):
  if(date!= ""):
    div= date.split("T")
    return div[0]+" "+(div[1])[:-1]