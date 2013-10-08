define sum 
proc(n)
i := n;
s := 0;
while i do s := s + i;  i := i-1 od;
return := s
end;
a:=1+3;
w:=[1,2,[
3,4]];
q := listp(2);
r := listp([]);
t:=nullp([]);
u:=cons(1,[[3,4]]);
v:=car([1,[2,3]]);
z:=cdr([1,[2,3],4]);
x := intp(2);
y := intp([]);
if x then
s := sum(x)
else
x := 0
fi