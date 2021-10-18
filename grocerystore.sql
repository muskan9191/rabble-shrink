-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 04, 2021 at 06:28 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `grocerystore`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `c_id` int(11) NOT NULL,
  `category` varchar(30) NOT NULL,
  `merchant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`c_id`, `category`, `merchant_id`) VALUES
(101, 'Tooth Paste', 1),
(102, 'Shampoo', 1),
(103, 'Body Lotion', 1),
(104, 'Pulses', 1),
(105, 'Oil', 1),
(106, 'Flour', 1),
(107, 'Rice', 1),
(108, 'Biscuits', 1),
(109, 'Tooth Brush', 1),
(110, 'Pencil', 2),
(111, 'Eraser', 2),
(112, 'pen', 2),
(113, 'Sheet', 2),
(114, 'Pouch', 2),
(115, 'Colours', 2),
(116, 'Notebook', 2),
(118, 'files', 2),
(119, 'folders', 2),
(120, 'Geometery Box', 2),
(121, 'Tooth Paste', 5),
(122, 'Oil', 5),
(123, 'Shampoo', 5),
(124, 'Tooth Brush', 5),
(125, 'Pulses', 5),
(126, 'Flour', 5),
(127, 'spices', 1),
(128, 'Toast', 1),
(129, 'Sanitizer', 1),
(130, 'Tea Leaves', 1);

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `srno` int(11) NOT NULL,
  `feedback` varchar(10) NOT NULL,
  `description` text NOT NULL,
  `merchant_id` int(11) NOT NULL,
  `order_id` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`srno`, `feedback`, `description`, `merchant_id`, `order_id`) VALUES
(3, 'Mediocre', 'good experience', 1, 'ORD-12423021744822'),
(4, 'Very good', 'Thanks for your service', 1, 'ORD-12423021744822');

-- --------------------------------------------------------

--
-- Table structure for table `merchant`
--

CREATE TABLE `merchant` (
  `merchant_id` int(11) NOT NULL,
  `shop_name` varchar(30) NOT NULL,
  `gst_no` int(11) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `uname` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `phone` char(10) NOT NULL,
  `address` text NOT NULL,
  `pincode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `merchant`
--

INSERT INTO `merchant` (`merchant_id`, `shop_name`, `gst_no`, `fname`, `lname`, `gender`, `uname`, `password`, `phone`, `address`, `pincode`) VALUES
(1, 'Vijay Stores', 2147483647, 'Vijay', 'Khurana', 'male', 'vcstores', '123456', '8978675612', 'Krukchetra, Dhaka', 440011),
(2, 'Malewar Book Store', 1234483647, 'Parag', 'Malewar', 'male', 'malewarbook', '123456', '9876123456', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara', 440011),
(3, 'Prashant Kirana Store', 1147483647, 'Prashant ', 'Jaiyantilal', 'male', 'prashant', '123456', '8967450213', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara', 441912),
(4, 'Heera Agency', 2111483647, 'Sunil', 'Madhwani', 'male', 'madhwani', '123456', '8967123450', 'Shri Ram Nagar Tumsar', 441932),
(5, 'Mahavir Kirana Store', 2009432607, 'Suresh ', 'Jain', 'male', 'sjain', '123456', '9878987899', 'Jivan Niwas', 440011),
(6, 'Kailash General Store', 1147483647, 'Kailash', 'Makhijani', 'male', 'kmgs', '123456', '9876123459', 'ghraisoni khapa', 441917),
(7, 'Jhethalal Gada', 1140483647, 'Jhethalal', 'Gada', 'male', 'jgada', '123456', '8778899654', 'Gokuldham Society', 441916),
(8, 'Scales Stationary', 1247483647, 'Yash', 'Jain', 'male', 'yjain', '123456', '9867126534', 'Hudkeshwar, Nagpur', 441919),
(9, 'Dayanand Kirana', 1907483647, 'Dayanand ', 'Mehta', 'male', 'dmehta', '123456', '9867547621', 'Mehta Niwas', 441915),
(10, 'Yashraj General Store', 1677483647, 'Yash', 'Garg', 'male', 'ygarg', '123456', '8976456754', 'Hemlata Square, Varthi', 441920),
(11, 'Umang Stationary ', 2097483647, 'Umang', 'Saraf', 'male', 'usaraf', '123456', '9867543610', 'Gokuldham Society', 441911);

-- --------------------------------------------------------

--
-- Table structure for table `orderplaced`
--

CREATE TABLE `orderplaced` (
  `srno` int(11) NOT NULL,
  `order_id` varchar(30) NOT NULL,
  `user_id` int(11) NOT NULL,
  `cust_name` varchar(30) NOT NULL,
  `amount` float NOT NULL,
  `merchant_id` int(11) NOT NULL,
  `Date` date NOT NULL DEFAULT current_timestamp(),
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderplaced`
--

INSERT INTO `orderplaced` (`srno`, `order_id`, `user_id`, `cust_name`, `amount`, `merchant_id`, `Date`, `status`) VALUES
(16, 'ORD-12423021744822', 1, 'Shreedha Lanjewar', 90, 1, '2021-01-22', 'Completed'),
(17, 'ORD-13542168915587', 1, 'Shreedha Lanjewar', 420, 1, '2021-01-22', 'Completed'),
(18, 'ORD-14768469974269', 1, 'Shreedha Lanjewar', 40, 1, '2021-01-22', 'Completed'),
(19, 'ORD-19911638321538', 1, 'Shreedha Lanjewar', 720, 1, '2021-01-22', 'Completed'),
(20, 'ORD-11667548332109', 1, 'Muskan', 200, 1, '2021-01-23', 'Completed'),
(21, 'ORD-17699315066992', 1, 'Shreedha Lanjewar', 360, 1, '2021-02-06', 'Completed'),
(22, 'ORD-18434191217221', 1, 'Muskan Madhwani', 120, 1, '2021-02-21', 'Completed');

-- --------------------------------------------------------

--
-- Table structure for table `orderproducts`
--

CREATE TABLE `orderproducts` (
  `sno` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `order_id` varchar(30) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderproducts`
--

INSERT INTO `orderproducts` (`sno`, `product_id`, `order_id`, `quantity`) VALUES
(45, 1, 'ORD-12423021744822', 2),
(46, 4, 'ORD-12423021744822', 1),
(47, 2, 'ORD-13542168915587', 1),
(48, 22, 'ORD-13542168915587', 1),
(49, 5, 'ORD-14768469974269', 1),
(50, 6, 'ORD-14768469974269', 1),
(51, 18, 'ORD-19911638321538', 2),
(52, 19, 'ORD-19911638321538', 1),
(53, 20, 'ORD-19911638321538', 2),
(54, 21, 'ORD-19911638321538', 2),
(55, 13, 'ORD-11667548332109', 1),
(56, 15, 'ORD-11667548332109', 1),
(57, 17, 'ORD-11667548332109', 2),
(58, 1, 'ORD-17699315066992', 1),
(59, 2, 'ORD-17699315066992', 1),
(60, 4, 'ORD-17699315066992', 1),
(61, 33, 'ORD-18434191217221', 2);

-- --------------------------------------------------------

--
-- Table structure for table `productlist`
--

CREATE TABLE `productlist` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `category` varchar(30) NOT NULL,
  `unit` varchar(5) NOT NULL,
  `img_name` varchar(30) NOT NULL,
  `price` float NOT NULL,
  `quantity` int(11) NOT NULL,
  `merchant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `productlist`
--

INSERT INTO `productlist` (`product_id`, `product_name`, `category`, `unit`, `img_name`, `price`, `quantity`, `merchant_id`) VALUES
(1, 'Dabar Babool Toothpaste 200g', 'Tooth Paste', 'item', 'babool.jpg', 30, 20, 1),
(2, 'Dove Shampoo 355ml', 'Shampoo', 'item', 'doveshampoo.jpg', 300, 10, 1),
(3, 'Lead Pencil', 'Pencil', 'item', 'leadpencil2.jpg', 20, 20, 2),
(4, 'Oral B Tooth Brush', 'Tooth Brush', 'item', 'oralbbrush.jpg', 30, 40, 1),
(5, 'Parle Biscuit', 'Biscuits', 'item', 'parleg.jpg', 5, 20, 1),
(6, 'Fortune Kachi Ghani Pure Mustard Oil 400ml', 'Oil', 'item', 'mustardoilsmall.jpg', 35, 20, 1),
(13, 'Colgate Max Fresh 170g', 'Tooth Paste', 'item', 'colmaxfresh.jpg', 60, 70, 1),
(14, 'Colgate Herbal 200g', 'Tooth Paste', 'item', 'colgateherbal.jpg', 50, 12, 1),
(15, 'Oral-B 3D white', 'Tooth Paste', 'item', 'oralbpaste.jpg', 60, 17, 1),
(16, 'Himalaya Sparkling White 150g', 'Tooth Paste', 'item', 'himalayasparkling.png', 30, 18, 1),
(17, 'Himalaya Mint Fresh 150g', 'Tooth Paste', 'item', 'himalaya.jpg', 40, 17, 1),
(18, 'Colgate Visible White 100g', 'Tooth Paste', 'item', 'visiblewhite.jpg', 40, 29, 1),
(19, 'Pepsodent Whitening 200g', 'Tooth Paste', 'item', 'pepsodent.jpg', 40, 32, 1),
(20, 'Fortune Sunlight Oil 250ml', 'Oil', 'item', 'sunfloweroil.jpg', 100, 10, 1),
(21, 'Fortune Kachi Ghani Pure Mustard Oil 1l', 'Oil', 'item', 'mustardoil.jpg', 200, 10, 1),
(22, 'Fortune Rice Bran Oil 1l', 'Oil', 'item', 'fortunepack.jpg', 120, 10, 1),
(23, 'Fortune Sunlight Oil 10l', 'Oil', 'item', 'fortunesunfloweroil.jpg', 1200, 10, 1),
(24, 'Dabar Babool Toothpaste 200g', 'Tooth Paste', 'item', 'babool.jpg', 30, 20, 5),
(25, 'Colgate Herbal Toothpaste 200g', 'Tooth Paste', 'item', 'colgateherbal.jpg', 50, 10, 5),
(26, 'Colgate Max Fresh 170g', 'Tooth Paste', 'item', 'colmaxfresh.jpg', 60, 10, 5),
(27, 'Oral-B 3D white', 'Tooth Paste', 'item', 'oralbpaste.jpg', 60, 10, 5),
(28, 'Pepsodent Whitening 200g', 'Tooth Paste', 'item', 'pepsodent.jpg', 40, 10, 5),
(30, 'Colgate Visible White 100g', 'Tooth Paste', 'item', 'visiblewhite.jpg', 40, 10, 5),
(31, 'Himalaya Mint Fresh 150g', 'Tooth Paste', 'item', 'himalaya.jpg', 40, 10, 5),
(32, 'Himalaya Sparkling White 150g', 'Tooth Paste', 'item', 'himalayasparkling.png', 30, 10, 5),
(33, 'Lifebuoy Sanitizer 200ml', 'Sanitizer', 'item', 'lifebuoy.jpg', 60, 20, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `mail` varchar(30) NOT NULL,
  `uname` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `phone` char(10) NOT NULL,
  `address` text NOT NULL,
  `pincode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `fname`, `lname`, `gender`, `mail`, `uname`, `password`, `phone`, `address`, `pincode`) VALUES
(1, 'Shreedha', 'Lanjewar', 'female', 'pinkskyy185@gmail.com', 'slanjewar', '123456', '9876543210', 'Ramkrushna Nagar, Tumsar', 440011),
(2, 'Ruchita ', 'Pahune', 'female', '', 'Rpahune', '123456', '9870654321', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara, Near Bank Of India Tumsar', 440011),
(3, 'Mehar', 'Nagare', 'male', '', 'mnagare', '123456', '9876054321', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara, Near Bank Of India Tumsar', 441912),
(4, 'Muskan', 'Madhwani', 'female', '', 'mmadhwani', '123456', '9689164953', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara, Near Bank Of India Tumsar', 441912),
(5, 'Ashita', 'Pashine', 'female', '', 'apashine', '123456', '9874563210', 'Tilak Niwas Pondicherry', 441910),
(6, 'Janvi', 'Sarve', 'female', '', 'Janvi12', '123456', '8796504321', 'Ramdas peth', 441918),
(7, 'Lalit', 'Sharma', 'male', '', 'lalit21', '123456', '7676895943', 'Doremon Street', 441925),
(8, 'Swati ', 'Wahichor', 'female', '', 'swati89', '123456', '9876504321', 'Omkar Niwas', 441913),
(9, 'Manav', 'Kanoje', 'male', '', 'mkanoje', '123456', '9807651234', 'Krukchetra, Dhaka', 441910),
(10, 'Laxmi', 'Jiyan', 'male', '', 'ljiyan', '123456', '9874563210', 'Kiyam Nagar', 441917),
(11, 'Vikas', 'Bansod', 'male', '', 'vbansod', '123456', '9876541230', 'Yadav Nagar', 441930),
(12, 'Kiran', 'Bhoyar', 'female', '', 'kbhoyar', '123456', '789654210', 'Hemlata Square, Varthi', 441931),
(13, 'Rupal', 'Sharma', 'female', '', 'rsharma', '123456', '8907651243', 'Obekom Street ', 441924),
(14, 'Muskan', 'Madhwani', 'female', 'muskanmadhwani@gmail.com', 'muskan16', '123456', '+919689164', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara', 441912),
(15, 'Muskan', 'Madhwani', 'female', 'muskanmadhwani4@gmail.com', 'madhwani', '123456', '+919689164', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara', 441912),
(16, 'Muskan', 'Madhwani', 'female', 'muskanmadhwani16@gmail.com', 'muskan161', '123456', '+919689164', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara', 441912),
(17, 'Muskan', 'Madhwani', 'female', 'muskanmadhwani16@gmail.com', 'muskan163', '123456', '+919689164', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara', 441912),
(18, 'Muskan', 'Madhwani', 'female', 'muskanmadhwani@gmail.com', 'muskan1', '123456', '+919689164', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara', 441912),
(19, 'Muskan', 'Madhwani', 'female', 'muskanmadhwani47@gmail.com', 'muskan12', '123456', '+919689164', 'Ramkrushna Nagar Near Bank Of India Tumsar Tumsar District Bhandara', 441912);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `merchant`
--
ALTER TABLE `merchant`
  ADD PRIMARY KEY (`merchant_id`),
  ADD UNIQUE KEY `uname` (`uname`);

--
-- Indexes for table `orderplaced`
--
ALTER TABLE `orderplaced`
  ADD PRIMARY KEY (`srno`),
  ADD UNIQUE KEY `order_id` (`order_id`),
  ADD KEY `Date` (`Date`);

--
-- Indexes for table `orderproducts`
--
ALTER TABLE `orderproducts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `productlist`
--
ALTER TABLE `productlist`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=131;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `merchant`
--
ALTER TABLE `merchant`
  MODIFY `merchant_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `orderplaced`
--
ALTER TABLE `orderplaced`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `orderproducts`
--
ALTER TABLE `orderproducts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `productlist`
--
ALTER TABLE `productlist`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
