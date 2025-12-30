math.randomseed(os.time())

local t = {}
for i = 1, 5 do
    t[i] = {x = math.random(1,50), y = math.random(1,50)}
end

local mt = {
    __add = function(a,b)
        return {x = a.x + b.x, y = a.y + b.y}
    end,
    __tostring = function(a)
        return "("..math.floor(a.x)..","..math.floor(a.y)..")"
    end
}

for i=1,#t do
    setmetatable(t[i], mt)
end

local function f(tbl)
    local sum = {x=0, y=0}
    setmetatable(sum, mt)
    for i=1,#tbl do
        sum = sum + tbl[i]
    end
    return sum
end

local function g(tbl)
    local r = {}
    for i=1,#tbl do
        r[i] = setmetatable({x=tbl[i].x*math.sin(i), y=tbl[i].y*math.cos(i)}, mt)
    end
    return r
end

t = g(t)
local total = f(t)
print("Resultado final: "..tostring(total))
