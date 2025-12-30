const t = Array.from({length: 5}, () => ({x: Math.random()*100, y: Math.random()*100}));

const handler = {
    get: (obj, prop) => {
        if(prop === 'sum') return obj.x + obj.y;
        return obj[prop];
    },
    set: (obj, prop, value) => {
        obj[prop] = value * Math.random();
        return true;
    }
};

const proxied = t.map(v => new Proxy(v, handler));

function f(arr){
    return arr.reduce((acc, val, i) => {
        const noise = Math.sin(i) * Math.random() * val.sum;
        acc.x += val.x + noise;
        acc.y += val.y - noise;
        return acc;
    }, {x:0, y:0});
}

function g(arr){
    return arr.map((v,i) => {
        return new Proxy({
            x: v.x * Math.cos(i),
            y: v.y * Math.sin(i)
        }, handler);
    });
}

const chaos = g(proxied);
const total = f(chaos);

console.log("Resultado final:", total);
