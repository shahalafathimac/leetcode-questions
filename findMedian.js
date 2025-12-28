function findMedianSortedArrays(nums1, nums2) {
  let merged = [];
  let i = 0, j = 0;

 
  for (; i < nums1.length && j < nums2.length; ) {
    if (nums1[i] < nums2[j]) {
      merged.push(nums1[i]);
      i++;
    } else {
      merged.push(nums2[j]);
      j++;
    }
  }

  
  for (; i < nums1.length; i++) {
    merged.push(nums1[i]);
  }

  for (; j < nums2.length; j++) {
    merged.push(nums2[j]);
  }

  let mid = Math.floor(merged.length / 2);

  
  if (merged.length % 2 === 0) {
    return (merged[mid - 1] + merged[mid]) / 2;
  } else {
    return merged[mid];
  }
}


console.log(findMedianSortedArrays([1, 3], [2])); 
