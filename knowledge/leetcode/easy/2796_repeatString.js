String.prototype.replicate = function (times) {
    let result = "";
    while (times > 0) {
        result += this;
        times--;
    }
    return result;
}
