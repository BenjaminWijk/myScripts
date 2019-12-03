function multiply(a,b)
  if b == 0 or a == 0 then
    return 0
  end

  if b < 0 then
    return multiply(-a,-b)
  end

  if b == 1 then
    return a
  end

 return a + multiply(a,b-1)
end

a,b = io.read("*n","*n")

c = multiply(a,b)
print(c)


--[[
for i=1,10000 do 
  a = math.random(-5,5)
  b = math.random(-5,5)  
  c = multiply(a,b)
  if c ~= a*b then
    print(a .. " + " .. b .. " returned: " .. c)
    break
  end
end
--]]

  
  





