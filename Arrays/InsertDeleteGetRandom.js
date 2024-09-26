class RandomizedSet {
    constructor() {
        this.map = new Map();
        this.arr = [];
    }

    insert(val) {
        if (this.map.has(val)) {
            return false;
        }
        this.map.set(val, this.arr.length);
        this.arr.push(val);
        return true;
    }

    remove(val) {
        if (!this.map.has(val)) {
            return false;
        }
        let index = this.map.get(val);
        let lastElement = this.arr[this.arr.length - 1];
        this.arr[index] = lastElement;
        this.map.set(lastElement, index);
        this.arr.pop();
        this.map.delete(val);
        return true;
    }

    getRandom() {
        let randomIndex = Math.floor(Math.random() * this.arr.length);
        return this.arr[randomIndex];
    }
}
