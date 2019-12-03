function fizzBuzz(length)
  for i=1, length do
    foundMatch = false

    if i % 3 == 0 then
      io.write("Fizz")
      foundMatch = true
    end
    if i % 5 == 0 then
      io.write("Buzz")
      foundMatch = true
    end
    if foundMatch ~= true then
      io.write(i)
    end
  io.write("\n")
  end
end

fizzBuzz(100)

