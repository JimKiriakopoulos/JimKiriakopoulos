class ArithmosSygrisis{
  public static void main(String[] args){
   int x=Integer.parseInt(args[0]);
   String str;
   if (x>0){
	   str="positive";
   }
   else if(x<0){
	  str="negative";
    }
	else {
	  str ="neutral";
	}
	System.out.println(str);
  }
}
