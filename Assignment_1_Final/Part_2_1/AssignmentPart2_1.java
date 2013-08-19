/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author richardhart
 */
import java.io.Console;
public class AssignmentPart2_1 {

    int index = -1;
    String input_string = "(3,(43),2)x";
    String read_sequence = "";
    char Token = 'x';

    /**
     * @param args the command line arguments
     */
    public void Match_Number(char token) {
        if (isDigit(token)) {
            while (isDigit(Token)) {
                read_sequence = read_sequence + Token;
                GetToken();
            }
        } else {
            System.out.println("Error: expected" + Token + " but recieved " + token);
        }
    }

    public void Match(char token) {
        if (token == Token) {
            read_sequence = read_sequence + Token;
            GetToken();
        } else {
            System.out.println("Error: expected" + Token + " but recieved " + token);
        }
    }

    public void GetToken() {
        index = index + 1;
        Token = input_string.charAt(index);
    }

    public boolean isDigit(char token) {
        return (token >= '0' && token <= '9');
    }

    public void List() {
        Match('(');
        if (Token != ')') {
            seq();
        }
        Match(')');

    }

    public void seq() {
        elt();
        if (Token == ',') {

            Match(',');
            seq();
        }
    }

    public void elt() {
        if (Token == '(') {
            List();
        } else {
            Match_Number(Token);
        }

    }

    public void RunParser() {
		Console c = System.console();
		System.out.println("hello!");
        System.out.println(input_string);
		c.format(input_string);
        GetToken();
        List();
        System.out.println(read_sequence);
		c.format(input_string);
    }

    public static void main(String[] args) {
        AssignmentPart2_1 p = new AssignmentPart2_1();
        p.RunParser();
    }
}
