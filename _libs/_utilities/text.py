
BAR="="*80
bar="-"*80
Bar="-="*25

def print_title(title="", space=1, mark="->"):
  '''
    Print @p title after @p space times "\t" and @p mark.
  '''
  txt="\t"*space
  txt+=mark
  txt+=" "+title 
  print txt

def print_error(msg="", space=1, mark=" ERROR:"):
  '''
    Print @p msg after @p space times "\t" and @p mark.
  '''
  txt="\t"*space
  txt+=mark
  txt+=" "+msg
  print BAR + "\n" + txt + "\n" + BAR