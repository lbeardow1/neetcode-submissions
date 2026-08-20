class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        Map<Character, Integer> visitedCharacters = new HashMap<>();
        
        for (int r = 0, l = 0; r < s.length(); r++){
            char currentCharacter = s.charAt(r);
            if (visitedCharacters.containsKey(currentCharacter) && visitedCharacters.get(currentCharacter) >= l){
                l = visitedCharacters.get(currentCharacter) + 1;
            }
            maxLength = Math.max(maxLength, r - l + 1);
            visitedCharacters.put(currentCharacter, r);
        }
            
        return maxLength;
    }
}
