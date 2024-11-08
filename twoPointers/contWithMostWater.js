function maxArea(height) {
    let left = 0, right = height.length - 1, maxArea = 0;

    while (left < right) {
        const width = right - left;
        const area = width * Math.min(height[left], height[right]);
        maxArea = Math.max(maxArea, area);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
}
