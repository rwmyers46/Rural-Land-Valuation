## Image Processing for Machine Learning:

1000s of images are required to train a robust neural network. However, redundant images do not improve the model and contribute to overfitting. Further, a single null image file may cause the build to abort with errors after several epochs of fitting. Thus, ensuring images are unique, uncorrupted, and adhere to expected file formats is imperative.

The CV2 and OS modules can readily handle null image files; the real challenge lies in avoid duplicate images. To confirm uniqueness not only for newly downloaded images, but also to avoid adding duplicates to our existing image directory, a pairwise comparison of each image is required. The number of comparisons required can be computed using graph theory, treating images as nodes and combinations as edges.

The equation for calculating the number of edges K for a complete, undirected graph with n nodes: K = n(n - 1)/2. 

Thus, to ensure 1,000 images are unique we must make 499,500 comparisons. Starting with O(N^2) complexity, the processing load is further increased when we compare each image pair pixel by pixel, each having 3 RGB color channels. Since these pixelated pairwise comparisons are (to my knowledge) elemental to confirming image uniquity, I decided the best way to achieve computational efficiency was to focus on reducing the number of images to compare. While graph theory holds in a "brute force" approach, images have more attributes than nodes - which we can exploit for our reductionist aims. 

The `Image_Optimizer` function does precisely this by first sorting images by their dimensional sizes. Taking a list of (file_name, file_size) tuples as the argument, it first finds the number of unique sizes. These sizes are used as keys for two purposes: to create a `counts` dictionary to count the number of unique size occurences and for a `filtered_dict` dictionary to which we will append filenames.

The `filtered_dict` of {image_dimensions : file_names list} represents a grouped list of images with identical dimensions. This dictionary is returned so that the `Check_Duplicates` function only need compare images of the same size to each other.

#### Test Results:

* For 846 images, the brute force approach requires processing 357,435 image pairs. 

* Using Image_Optimizer's algorithm, images are divided into 87 unique size groups and a total of 2,139 pairs are processed.

* The top-level processing efficiency gain is 167x as only 0.598% of original combinations require further evaluation. 
