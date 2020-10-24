import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_variable_declar(self):
        #test variable declarations-5
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_variable_declara_2(self):
        
        input = """Var: a,b ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_variable_declara_initial(self):
        
        input = """Var: a=5 ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_variable_declara_initial_composite(self):
        
        input = """Var: a=5,b,c ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_variable_declara_contain_array(self):
        
        input = """Var: m,n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_variable_declara_random_composite(self):
        
        input = """Var:c,d=6,e,f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_wrong_Variable_declarations(self):
        
        input = """Var:c={4};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_multiline_variabledeclaration(self):
        input = """Var:c;
        Var:d=0,a;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_same_variable_declaration(self):
        input = """Var:a;
        Var:a,a;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_multiarray_variabledeclaration(self):
        input = """Var:a[9];
        Var:d[10][11];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    #test function declarations -10
    def test_function_declaration(self):
        input = """Function: fact
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_function_declaration_With_Parameter(self):
        input = """Function: fact
        Parameter: n
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_function_declaration_With_many_Parameter(self):
        input = """Function: fact
        Parameter: a,b,c
        Body:
        
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_function_declaration_With_composite_Parameter(self):
        input = """Function: fact
        Parameter: a[10],b[10]
        Body:
        
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_function_declaration_With_intial_Parameter(self):
        input = """Function: fact
        Parameter: a=12
        Body:
        
        EndBody.
        """
        expect = "Error on line 2 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_function_declaration_With_vardeclaration_inside(self):
        input = """Function: fact
        Body:
        Var: b[2][3]={{2,3,4},{4,5,6}};
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_function_declaration_With_var_declaration_inside(self):
        input = """Function: fact
        Body:
        Var: b[2]=5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_function_declaration_With_normal_declaration_inside(self):
        input = """Function: fact
        Parameter: a,b,c
        Body:
        Var: m=1,n=3;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_function_declaration_With_variable_inside(self):
        input = """Function: fact
        Parameter: a,b,c
        Body:
        a=4;
        b=5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_function_main(self):
        input = """Function: main
        Body:
        x=10;
        fact(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    #test variable declaration statement
    def test_variable_declaration_statement(self):
        input = """Function: main
        Body:
        Var:r=10.,v;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_variable_declaration_statement_2(self):
        input = """Function: main
        Body:
        Var:r=10.,v;
        v=(4.\.3.)*.3.14*.r*.r*.r;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_variable_declaration_statement_3(self):
        input = """Function: main
        Body:
        Var:r[5]={1,4,3,2,0};
        
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    #test assign statement
    def test_assign_statement(self):
        input = """Function: main
        Body:
        a=12.5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_assign_statement_composite(self):
        input = """Function: main
        Body:
        a[12]=90;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    #test if statement-10
    def test_if_statement(self):
        input = """Function: main
        Body:
        If a==3 Then a=5;
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_if_statement_without_statementlist(self):
        input = """Function: main
        Body:
        If a==3 Then
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_if_statement_without_statementlist_and_ElseIf(self):
        input = """Function: main
        Body:
        If a==3 Then
        ElseIf a>b Then
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_if_statement_without_statementlist_and_ElseIf_Else(self):
        input = """Function: main
        Body:
        If a==3 Then
        ElseIf a>b Then
        Else
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_if_statement_with_Else(self):
        input = """Function: main
        Body:
        If a==3 Then
        Else
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_if_statement_with_Else_statement(self):
        input = """Function: main
        Body:
        If a==3 Then a=a+1;
        Else b=0;
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_if_statement_with_ElseIf_statement(self):
        input = """Function: main
        Body:
        If a==3 Then a=a+1;
        ElseIf a>=9 Then c=b*5;
        Else b=0;
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_if_statement_with_ElseIf_multistatement(self):
        input = """Function: main
        Body:
        If a==3 Then 
        a=a+1;
        b=b+1;
        ElseIf a>=9 Then c=b*5;
        Else b=0;
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_if_statement_with_ElseIf_two_conditions(self):
        input = """Function: main
        Body:
        If (a==3) && (b==d) Then 
        a=a+1;
        b=b+1;
        ElseIf a>=9 Then 
        c=b*5;
        d=d+1;
        Else b=0;
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_if_statement_with_ElseIf_condition_on_elseif(self):
        input = """Function: main
        Body:
        If (a==3) && (b==d) Then
        a=a+1;
        b=b+1;
        ElseIf (a>=9) || (a<=5) Then 
        c=b*5;
        d=d+1;
        Else b=0;
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    #test for statement
    def test_for_statement(self):
        input = """Function: main
        Body:
        For(i=0,i<10,2)Do
        EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_for_statement_without_condition(self):
        input = """Function: main
        Body:
        For(i=0,,2)Do
        EndFor.
        EndBody.
        """
        expect = "Error on line 3 col 16: ,"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_for_statement_without_update(self):
        input = """Function: main
        Body:
        For(i=0,i<10,)Do
        EndFor.
        EndBody.
        """
        expect = "Error on line 3 col 21: )"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_for_statement_with_statementlist(self):
        input = """Function: main
        Body:
        For(i=0,i<10,2)Do
        a=a+1;
        EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_for_statement_with_updateExpr(self):
        input = """Function: main
        Body:
        For(i=0,i<=10,i+1)Do
        a=a+1;
        EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    #test while statement-5
    def test_while_statement(self):
        input = """Function: main
        Body:
        While a>1 Do
         
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_while_statement_with_statement_inside(self):
        input = """Function: main
        Body:
        While a>1 Do
        a=a+1; 
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_while_statement_with_someexpression_inside(self):
        input = """Function: main
        Body:
        While (a>1) && (b<2) Do
        a=a+1; 
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_while_statement_have_some_statements_inside(self):
        input = """Function: main
        Body:
        While (a>1) && (b<2) Do
        a=a+1;
        b=b*3;
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_while_statement_have_ifstatement_inside(self):
        input = """Function: main
        Body:
        While (a>1) && (b<2) Do
        If a==3 Then 
        a=a+1;
        EndIf.
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    #test do while statement-5
    def test_do_while_statement_nullable_statement(self):
        input = """Function: main
        Body:
        Do
        While a>3 EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_do_while_statement_have_statement_inside(self):
        input = """Function: main
        Body:
        Do
        a=a%10;
        While a>3 EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_do_while_statement_multiplication_float_inside(self):
        input = """Function: main
        Body:
        Do
        a=a%10;
        b=b*.3.15;
        While a>3 EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_do_while_statement_multi_expresion(self):
        input = """Function: main
        Body:
        Do
        a=a%10;
        b=b*.3.15;
        While (a>3) && (b<=100) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_do_while_statement_without_expresion(self):
        input = """Function: main
        Body:
        Do
        a=a%10;
        b=b*.3.15;
        While  EndDo.
        EndBody.
        """
        expect = "Error on line 6 col 15: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    #test call statement-5
    def test_call_statement(self):
        input = """Function: main
        Body:
        foo(2+x,4.\.y);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_call_statement_2(self):
        input = """Function: main
        Body:
        goo();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_call_statement_2_call_statement(self):
        input = """Function: main
        Body:
        foo(2+x,4.\.y);
        goo();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_call_statement_2_call_statement_with_float_number(self):
        input = """Function: main
        Body:
        foo(5.1);
      
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_call_statement_2_call_statement_integer_inside(self):
        input = """Function: main
        Body:
        goo(2);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    #test break, continue,return statement-10
    def test_break_statement(self):
        input = """Function: main
        Body:
        Break;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_break_statement_inside_for_loop(self):
        input = """Function: main
        Body:
        For(i=0,i<10,2)Do
        a=a+1;
        Break;
        EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_break_statement_inside_while_loop(self):
        input = """Function: main
        Body:
        While (a>1) && (b<2) Do
        a=a+1;
        b=b*3;
        Break;
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_break_statement_inside_dowhile_loop(self):
        input = """Function: main
        Body:
        Do
        a=a%10;
        b=b*.3.15;
        Break;
        While (a>3) && (b<=100) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_break_statement_inside_ifstatement(self):
        input = """Function: main
        Body:
        While (a>1) && (b<2) Do
        If a==3 Then 
        a=a+1;
        Break;
        EndIf.
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_continue_statement(self):
        input = """Function: main
        Body:
        Continue;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_continue_statement_inside_for_loop(self):
        input = """Function: main
        Body:
        For(i=5,i<10,i+2) Do
        Continue;
        EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_continue_statement_inside_while_loop(self):
        input = """Function: main
        Body:
        While(i<10) Do
        Continue;
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_continue_statement_inside_dowhile_loop(self):
        input = """Function: main
        Body:
        Do
        Continue;
        While i>10 EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_return_statement(self):
        input = """Function: main
        Body:
        Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_return_statement_with_expression(self):
        input = """Function: main
        Body:
        Return x;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_return_statement_return_functioncall(self):
        input = """Function: main
        Body:
        Return foo();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_return_statement_return_functioncall_expression(self):
        input = """Function: main
        Body:
        Return foo(x+1);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_return_statement_return_functioncall_float(self):
        input = """Function: main
        Body:
        Return foo(5.6);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_return_statement_return_expression(self):
        input = """Function: main
        Body:
        Return x+4;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    #test index operator, function call-10
    def test_index_operator_1(self):
        input = """Function: main
        Body:
        a[3]=9;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_index_operator_with_function_call(self):
        input = """Function: main
        Body:
        a[5]=foo(4);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_vardeclar_with_while_loop(self):
        input = """Function: foo
        Parameter: a[5],b
        Body:
        Var: i=0;
        While(i<5) Do
        c=b+.1.0;
        i=i+1;
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_vardeclar_with_for_loop(self):
        input = """Function: foo
        Parameter: a[5],b
        Body:
        Var: i=0;
        For(i=0,i<10,i+1) Do
        c=b+.1.0;
        i=i+1;
        EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_vardeclar_with_dowhile_loop(self):
        input = """Function: foo
        Parameter: a[5],b
        Body:
        Var: i=0;
        Do
        c=b+.1.0;
        i=i+1;
        While(i>10) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_index_operator_with_dowhile_loop(self):
        input = """Function: foo
        Parameter: a[5],b
        Body:
        Var: i=0;
        Do
        c[i-1]=b+.1.0;
        i=i+1;
        While(i>10) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_index_operator(self):
        input = """Function: foo
        Parameter: a[5],b
        Body:
        a[3+4]= 3+4;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_index_operator_2(self):
        input = """Function: foo
        Parameter: a[5],b
        Body:
        a[3+4]= 3+4;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    
    def test_var_func_declar(self):
        input = """Function: fact
        Parameter: n
        Body:
        If n==0 Then
        Return 1;
        Else
        Return n*fact(n-1);
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_while_in_func_declar(self):
        input = """Function: fact
        Parameter: a[5],b
        Body:
        Var: i=0;
        While i<5 Do
        a[i]=b+.10.0;
        i=i+1;
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_index_expression(self):
        input = """Function: fact
        Body:
        a[3+foo(2)]=4;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_index_expression_with_multiarray(self):
        input = """Function: fact
        Body:
        a[3+foo(2)]=a[b[2][3]]+4;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_Variable15(self):
        """Miss variable"""
        input = """Var: a = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_ifstatement_in_for_loop(self):
        """Miss variable"""
        input = """Function: foo
        Body:
        For(i=0,i<9,i+1)Do
        If i==3 Then
        Continue;
        EndIf.
        EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_ifstatement_in_while_loop(self):
        """Miss variable"""
        input = """Function: foo
        Body:
        While i==0 Do
        If i==3 Then
        Continue;
        EndIf.
        EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_if_else_statement_many(self):
        """Miss variable"""
        input = """Function: foo
        Body:
        If i==3 Then
        a=3;
        Else
        EndIf.
        If i>0 Then
        b=5;
        EndIf.
        
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_simple_function_declaration_statement(self):
        input = """Function: foo
        Parameter: a,b
        Body:
        Var: a,b;
        t=a+b;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_simple_function_declaration_statement2(self):
        input = """Function: foo
        Parameter: a,b
        Body:
        Var: a,b;
        t=a+b;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_pow_function_statement(self):
        input = """Function:foo
            Body:
	                Var: result;
	                For(i = 1, i <= exponential, i+1)Do
		                 result = result*base;
                    EndFor.
	                Return result;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))
    def test_abs_function_statement(self):
        input = """ Function: myAbs
                Parameter: value
                Body:
    
	            If value < 0 Then
		          Return -8;
	            Else
		         Return value;
                 EndIf.
                
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    def test_simple_functioncall_with_swapnum_statement(self):
        input = """ Function: swapnum
            Parameter: var1, var2
            Body:
            Var: tempnum;
            tempnum=var1;
            var1=var2;
            var2=tempnum;
            EndBody.
            
            Function: main
            Body:
                 swapnum(num1,num2);
            
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))
    def test_not_expression_statement(self):
        input = """
               Function: main
               Body:
                    a=!b;
               EndBody.  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
    def test_multiplus_expression_statement(self):
        input = """
                Function: main
                Body:
                    i=1+1+2+3;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))
    def test_multiply_expression(self):
        input = """ Function: main
                    Body:
                    Var: n, i;
                    n = 5 =6 - 9 *(10-8\\6) - p[2];
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
    def test_primenumber_program(self):
        input = """ Function: main
                    Body:
                    Var: a,i,m,flag;
                    m=n\\2;
                                   For(i=2,i<=m,i+1)Do
                                   If n%i==0 Then
                                   
                                   flag=1;
                                   Break;
                                   EndIf.
                                   
                                   If flag==0 Then
                                   Return 0;
                                   EndIf.
                    EndFor.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))
    def test_palindrome_program(self):
        input = """ Function: main
                    Body:
                                   Var: n,r,sum,temp;
                                   temp=n;
                                   Do
                                   r=n%10;
                                   sum=(sum*10)+r;
                                   n=n\\10;
                                   While n>0 EndDo.
                                   If temp==sum Then
                                   a=1;
                                   Else
                                   Return 0;
                                   EndIf.
                                   
                    EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    def test_armstrongnumber_program(self):
        input = """ Function: main
                    Body:
                                   Var: n,r,sum,temp;
                                   temp=n;
                                   Do
                                   r=n%10;
                                   sum=sum+(r*r*r);
                                   n=n\\10;
                                   While n>0 EndDo.
                                   If temp==sum Then
                                   a=1;
                                   Else
                                   Return 0;
                                   EndIf.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    def test_swapnumber_program(self):
        input = """Function: main
                Body:
                                   Var: a,b;
                                   a=10;
                                   b=20;
                                   a=a+b;
                                   b=a-b;
                                   a=a-b;
                                   Return 0;
                        
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    def test_function_declaration_check_statement(self):
        input = """
                Function: checkingdivision
                Parameter: n
                Body:
                   If ((n % 2) == 0) && ((n % 5) == 0) Then
                    Return 1;
                   Else
                    Return 0;
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
    def test_mutiblock_with_statementinside(self):
        input = """Function: main
        Body:
                Var: a,b;
                If a>b Then
                a=a+1;
                EndIf.
                a=b+1;   
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))


      