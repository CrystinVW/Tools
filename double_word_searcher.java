import java.io.*;
import java.util.*;
 
 
public class DuplicateWordSearcher {
    // Define Constants
	static final String INPUT_FILE = "words.txt";
	static final String OUTPUT_FILE = "concordance.txt";
	
	public static void main (String [] args) throws Exception {
	
		// Access IO Files
		File inputDataFile = new File(INPUT_FILE);
		Scanner inputFile = new Scanner(inputDataFile);
		FileWriter outputDataFile = new FileWriter(OUTPUT_FILE);
		PrintWriter outputFile = new PrintWriter(outputDataFile, true);
		System.out.println("Reading file " + INPUT_FILE + "\n" + 
				             "Creating file " + OUTPUT_FILE);
    
    
      while (inputFile.hasNext()) {  
        String text = inputFile.nextLine();         
        List<String> list = Arrays.asList(text.split(" "));
        Set<String> uniqueWords = new HashSet<String>(list);
        
        for (String word : uniqueWords) {
            if (uniqueWords.contains(word)) {
               uniqueWords.delete(word);
              
            }   
            System.out.println(word.toLowerCase() + ": " + Collections.frequency(list, word));
        }
      }
      
      inputFile.close();
	   outputFile.close();
	   System.exit(0);    
    }   
}
