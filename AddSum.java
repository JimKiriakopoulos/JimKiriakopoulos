class AddSum{
 public static void main(String[] args){
  int x=Integer.parseInt(args[0]);
  int y=Integer.parseInt(args[1]);
  String r="Addition";
  String p="Subtraction";
  System.out.println(r+":"+(x+y));
  System.out.println(p+":"+(x-y));
  int z=x;
  int m=y;
  String e="einai arithmos";
  System.out.printf("%s %s:%d\n",r,e,z+m);
  System.out.printf("%s %s:%d",p,e,z-m);
 }
}