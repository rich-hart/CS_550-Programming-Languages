define sum 
proc(n)
i := n;
s := 0;
while i do s := s + i;  i := i-1 od;
return := s
end;
y:=[1,2,[
3,4]];
z:=1+1;
x := 2;
s := 0;
if x then
s := sum(x)
else
x := 0
fi
