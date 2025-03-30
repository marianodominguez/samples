import java.util.*;


class BinarySearch {
  public static int find(ArrayList<Integer> a, int element) {
    int lower=0;
    int upper=a.size()-1;
        
    while (lower < upper) {
      
      int middle= lower + (upper - lower) /2 ;
      int current = a.get(middle);

      
      if(current == element) {
        return middle;
      }
      if ( current < element)  {
        lower = middle+1;
      }
      else {
        upper = middle-1;
      }
      
      //System.out.println( lower + ", " + upper +  " middle: " + middle);
    }
    
    return -1;
  }
  
  public static int findFirst(ArrayList<Integer> a, int element) { 
    int lower =0;
    int upper =a.size()-1;
    int result=-1;
    
    while(lower <= upper) {
      int middle = lower + (upper - lower)/2;
      int current = a.get(middle);
      
      if (current == element) {
        if( middle == 0 || a.get(middle-1) < element ) result = middle;
      }
      if (current < element) {
        lower = middle + 1;
      } 
      else {
        upper = middle -1;
      }

    }
    return result;
  }
  
  
  public static int findLast(ArrayList<Integer> a, int element) {
    int lower=0;
    int upper=a.size()-1;
    int result = -1;
    
    
    while (lower <= upper) {
      int middle = lower + (upper - lower)/2;
      int current = a.get(middle);
      if (current == element) {
        if ( middle==a.size()-1 || a.get(middle+1) > element) result = middle; 
      }
      if (current <= element) {
        lower = middle + 1;
      }
      else {
        upper = middle -1;
      }
        
    }
    
    
    return result;
  }
  
}


class Solution {

  public static void main(String[] args) {
    ArrayList<Integer> a = new ArrayList<>();
    
    a.addAll( Arrays.asList(1,2,3,4,5,5,5,5,5,5,6,7,7,8,10) );
    
    System.out.println( BinarySearch.findFirst(a, 7) );
    System.out.println( BinarySearch.findFirst(a, 2) );
    System.out.println( BinarySearch.findFirst(a, 4) );
    System.out.println( BinarySearch.findFirst(a, 5) );
    System.out.println( BinarySearch.findFirst(a, -1) ); 
    
    
    System.out.println( BinarySearch.findLast(a, 7) );
    System.out.println( BinarySearch.findLast(a, 2) );
    System.out.println( BinarySearch.findLast(a, 4) );
    System.out.println( BinarySearch.findLast(a, 5) );
    System.out.println( BinarySearch.findLast(a, -1) ); 
    
    System.out.println( BinarySearch.find(a, 7) );
    System.out.println( BinarySearch.find(a, 2) );
    System.out.println( BinarySearch.find(a, 4) );
    System.out.println( BinarySearch.find(a, 5) );
    System.out.println( BinarySearch.find(a, -1) ); 
  }
}



