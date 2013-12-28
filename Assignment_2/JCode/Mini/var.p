define sum 
proc(n)
  i := n;
  s := 0;
  while i do s := s + i;  i := i-1 od;
  a := 1 + s;
  return := a
end;

y :=5;
x := 7 + y;
if x then
  s := sum(x)
else
  x := 0 - x
fi

