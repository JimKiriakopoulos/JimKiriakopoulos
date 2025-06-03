class ArithmiPrajois{
 public static void main(String[] args){
   int x = Integer.parseInt(args[0]);
   int y = Integer.parseInt(args[1]);
   System.out.printf("%d + %d = %d\n",x,y,(x+y));
   System.out.printf("%d - %d = %d\n",x,y,(x-y));
   System.out.printf("%d * %d = %d\n",x,y,(x*y));
   System.out.printf("%d / %d = %d",x,y,(x/y));
 }
}