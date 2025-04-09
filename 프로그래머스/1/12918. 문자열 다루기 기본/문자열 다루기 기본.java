class Solution {
    public boolean solution(String s) {
        
        char[] array = s.toCharArray();
        if(!(array.length == 4 || array.length == 6)){
            return false;
        }
        for(char a : array) {
            if(a < '0' || a > '9') {
                return false;
            }
        }
        return true;
    }
}