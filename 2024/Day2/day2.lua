print("Day 2")

local file = io.open("day2_input.txt", "r")
local safe = 0

local function issave(level)
    if table.sort(level) == level or table.sort(level, function(x, y) return x > y end) then
        return 0
    end
    for i, num in ipairs(level) do
        if i ~= 0 then
            i = i -1
            if math.abs(num - level[#level-i - 1]) > 2 then
                return false
            end
        end
    end
    return true
end


if file ~= nil then
    for line in file:lines("l") do
        local numbers = {}
        for str in string.gmatch(line, "([^" .. "%s" .. "]+)") do
            table.insert(numbers, tonumber(str, 10))
        end
        if issave(numbers) then
            safe = safe + 1
        end
    end
end

print(safe)
