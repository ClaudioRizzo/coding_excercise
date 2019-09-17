import java.util.HashMap;
import java.util.Map;

public class Steps {

    private static Map<Integer, Integer> cache = new HashMap<>();  

    public static int steps(int stepNumber) {
        // This has 2^(n-1), just draw the invocation tree
        if(stepNumber < 0){
            return 0;
        } else if(stepNumber == 0) {
            return 1;
        } else {
            return steps(stepNumber-1) + steps(stepNumber-2);
        }

    }

    public static int efficientSteps(int stepNumber) {
        
        if(cache.containsKey(stepNumber)) {
           
            return cache.get(stepNumber);
        } else if(stepNumber == 0) {
            cache.put(stepNumber, 1);
            return 1;
        } else {
            
            cache.put(stepNumber-1, steps(stepNumber-1));
            cache.put(stepNumber-2, steps(stepNumber-2));
            System.out.println(cache.keySet());
            return cache.get(stepNumber-1) + cache.get(stepNumber-2);
        }
    }

    public static void main(String[] args) {
        System.out.println("Steps: "+efficientSteps(5));
    }
}