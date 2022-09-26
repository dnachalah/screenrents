-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 26, 2022 at 10:25 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rentalsapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` int(255) NOT NULL,
  `firstname` text NOT NULL,
  `lastname` text NOT NULL,
  `email` longtext NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_picture` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`, `firstname`, `lastname`, `email`, `password`, `profile_picture`) VALUES
(1, 'ay', 'ay', 'ayodelea@proxynetgroup.com', '12345678', ''),
(2, 'Benjamin', 'Noel', 'diaphorosnachalah40@gmail.com', '11111111', ''),
(3, 'Ben', 'Ben', 'diaphorosnachalah@gmail.com', '22222222', '');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add rentalsapp', 7, 'add_rentalsapp'),
(26, 'Can change rentalsapp', 7, 'change_rentalsapp'),
(27, 'Can delete rentalsapp', 7, 'delete_rentalsapp'),
(28, 'Can view rentalsapp', 7, 'view_rentalsapp'),
(29, 'Can add subscription', 8, 'add_subscription'),
(30, 'Can change subscription', 8, 'change_subscription'),
(31, 'Can delete subscription', 8, 'delete_subscription'),
(32, 'Can view subscription', 8, 'view_subscription'),
(33, 'Can add categories', 9, 'add_categories'),
(34, 'Can change categories', 9, 'change_categories'),
(35, 'Can delete categories', 9, 'delete_categories'),
(36, 'Can view categories', 9, 'view_categories'),
(37, 'Can add brands', 10, 'add_brands'),
(38, 'Can change brands', 10, 'change_brands'),
(39, 'Can delete brands', 10, 'delete_brands'),
(40, 'Can view brands', 10, 'view_brands'),
(41, 'Can add screens', 11, 'add_screens'),
(42, 'Can change screens', 11, 'change_screens'),
(43, 'Can delete screens', 11, 'delete_screens'),
(44, 'Can view screens', 11, 'view_screens'),
(45, 'Can add screenbookings', 12, 'add_screenbookings'),
(46, 'Can change screenbookings', 12, 'change_screenbookings'),
(47, 'Can delete screenbookings', 12, 'delete_screenbookings'),
(48, 'Can view screenbookings', 12, 'view_screenbookings'),
(49, 'Can add admin', 13, 'add_admin'),
(50, 'Can change admin', 13, 'change_admin'),
(51, 'Can delete admin', 13, 'delete_admin'),
(52, 'Can view admin', 13, 'view_admin'),
(53, 'Can add contacts', 14, 'add_contacts'),
(54, 'Can change contacts', 14, 'change_contacts'),
(55, 'Can delete contacts', 14, 'delete_contacts'),
(56, 'Can view contacts', 14, 'view_contacts');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `brandd`
--

CREATE TABLE `brandd` (
  `id` int(255) NOT NULL,
  `brand` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `brandd`
--

INSERT INTO `brandd` (`id`, `brand`) VALUES
(1, 'Maxhub'),
(2, 'Samsung'),
(3, 'LG'),
(5, 'Vestel');

-- --------------------------------------------------------

--
-- Table structure for table `categoryy`
--

CREATE TABLE `categoryy` (
  `id` int(255) NOT NULL,
  `category` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categoryy`
--

INSERT INTO `categoryy` (`id`, `category`) VALUES
(1, 'Rentals Screen'),
(2, 'Video Conferencing');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `id` int(255) NOT NULL,
  `name` int(255) NOT NULL,
  `email` longtext NOT NULL,
  `phone` varchar(255) NOT NULL,
  `subject` longtext NOT NULL,
  `message` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(13, 'rentalsapp', 'admin'),
(10, 'rentalsapp', 'brands'),
(9, 'rentalsapp', 'categories'),
(14, 'rentalsapp', 'contacts'),
(7, 'rentalsapp', 'rentalsapp'),
(12, 'rentalsapp', 'screenbookings'),
(11, 'rentalsapp', 'screens'),
(8, 'rentalsapp', 'subscription'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-09-20 09:02:20.411383'),
(2, 'auth', '0001_initial', '2022-09-20 09:02:20.911494'),
(3, 'admin', '0001_initial', '2022-09-20 09:02:21.041611'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-09-20 09:02:21.056757'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-09-20 09:02:21.061275'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-09-20 09:02:21.131247'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-09-20 09:02:21.211586'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-09-20 09:02:21.231434'),
(9, 'auth', '0004_alter_user_username_opts', '2022-09-20 09:02:21.241328'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-09-20 09:02:21.297482'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-09-20 09:02:21.301492'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-09-20 09:02:21.313575'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-09-20 09:02:21.336489'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-09-20 09:02:21.361271'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-09-20 09:02:21.381265'),
(16, 'auth', '0011_update_proxy_permissions', '2022-09-20 09:02:21.401396'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-09-20 09:02:21.446268'),
(18, 'sessions', '0001_initial', '2022-09-20 09:02:21.491449');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('qeo3t8xaym95mbh5l545r6tqbnz39swi', '.eJwtyTEOgCAQRNG7TE0DJZchgJOocZEsWBjj3d3C8v3_YPBgnR4RAe5XMHlT17NT553SYNa6WrYqlEJN24LoHa5BbVlor7DtWbaG9wOyahwn:1oaevZ:8VwAEaVWD49UIkbjxklLGF4fBkDqBZCnWl2QG9BFxzg', '2022-10-04 15:12:49.514238'),
('xy4dqze8cxgwfadh70kdcvqlfi06t0qh', 'eyJhZG1pbl9pZCI6Mn0:1oaf0o:lZhESZjLZcmCeRpWDRbfsHYbXkN2nRYJnpkUsZ6lsLI', '2022-10-04 15:18:14.153313');

-- --------------------------------------------------------

--
-- Table structure for table `screenss`
--

CREATE TABLE `screenss` (
  `id` int(255) NOT NULL,
  `screenname` longtext NOT NULL,
  `description` longtext NOT NULL,
  `date_added` date NOT NULL,
  `added_by` text NOT NULL,
  `updated_by` text NOT NULL,
  `price` longtext NOT NULL,
  `picture` longtext NOT NULL,
  `category_id` int(255) NOT NULL,
  `brand_id` int(255) NOT NULL,
  `dimension` longtext NOT NULL,
  `quantity` int(255) NOT NULL,
  `short_description` varchar(5000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `screenss`
--

INSERT INTO `screenss` (`id`, `screenname`, `description`, `date_added`, `added_by`, `updated_by`, `price`, `picture`, `category_id`, `brand_id`, `dimension`, `quantity`, `short_description`) VALUES
(1, 'MAXHUB 75 INCHES INTERACTIVE INTELIGENT PANEL - S75FA', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">75 INCHES INTERACTIVE INTELLIGENT PANEL DESIGNED FOR EDUCATION</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The MAXHUB Collaborative Interactive Display is an interactive UHD screen featuring extensive Collaboration and Whiteboarding software, and Wireless connectivity all form part of the package. This interactive touch screen is especially popular in the Educational Industry and Corporate environments. Due to its versatile functionality and different sizes on offer, there is also a growing demand for MAXHUB in huddle spaces, medium- and large-sized meeting rooms, and boardrooms. These impressive screens offer an all-inclusive solution; camera, microphone, front-firing speakers, Intelligent Graphic and Writing Recognition, Interactive Mirroring for up to 4 devices, Pre-loaded whiteboarding, interactive collaboration software, and even cloud storing.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">MAXHUB series is easy to set up and is the perfect COLLABORATION SOLUTION for Smart classrooms, Huddle spaces, and Boardrooms. Features one physical power button bottom loudspeaker4K ultra HD display IR (Infrared Ray) touch technology AG tempered glass 4mm Mohs level 7 Compatible with detachable PC module USB 3.0 Auto switch to android front USB 2.0 Auto switch to current channel low parallax, 1 mm air gap Android 8.<br><br></p><ul style=\"color: rgb(104, 113, 136);\"><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. Thin and extraordinary appearance</span><br>Highly integrated triple cameras design, six array microphones, and three sets of speakers, with a 19mm thin and flat appearance, making your work space neat and superior.</p></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. 88.9% Screen-to-body ratio provides your broader horizon</span><br>4K Ultra-large interactive screen, 88.9% screen-to-body ratio, direct bonding technology, and anti-glare technology present your clear image and broad horizon.</p></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. Intelligent writing frees your imagination - 0.04s Rapid Response Time, 1024 Levels Pressure Sensitivity, 0.5mm Touch Accuracy, Smart Graphics Assistant</span></p></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. Screen Writing is superior to paper writing</span><br>Projected capacitive and EMR combined touch technology creates 0.04s response time and brings your fluent and instantaneous writing experience. 1024 levels pressure sensitivity offers pixel-perfect precision and unmatched versatility.</p></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. Free annotation records your inspiration</span><br>Annotation is available at any interface to record your inspiration. When playing PPT, your annotation can be individually created in every page and easily saved.</p></li><li style=\"margin-left: 20px;\"><span style=\"font-weight: bolder;\">. Smart assistant writing makes your work easier.</span><br>Dual-pen and Dual-color writing, matched with innovative graphic intelligent recognition technology, table insertion and smart gesture control, simplifies your work</li><li style=\"margin-left: 20px;\"><br></li></ul><ul style=\"color: rgb(104, 113, 136);\"><li style=\"margin-left: 20px;\"><span style=\"font-weight: bolder;\">. Convenient saving and sharing the meeting records</span><br>Conference documents and records can be easily stored and shared by email and reedited next time as well.</li><li style=\"margin-left: 20px;\"><br></li></ul><ul style=\"color: rgb(104, 113, 136);\"><li style=\"margin-left: 20px;\"><span style=\"font-weight: bolder;\">. Multi-screen interaction eliminates the cable limitation - 0.09s Wireless Share Response Time, Synchronous Sharing with Mobile Device, Control Back Devices through MAXHUB 4-split Screen Mirroring,&nbsp;</span><b>Touch and Share, synchronous mirroring can be done through mobile devices</b></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Free multi-terminals connection can be achieved on PC or mobile device with wireless mirroring and related software, supporting up to 4 devices mirroring simultaneously and providing you clear comparison of presentation.</p></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. Real time mirroring presents fluently and stably</span><br>0.09s transmission time is unlikely to be noticed by the naked eye. The presentation of HD pictures and videos can still be clear and fluent.</p></li><li style=\"margin-left: 20px;\"><span style=\"font-weight: bolder;\">. Double-directional operation creates flexible and efficient interaction</span><br>With MAXHUB wireless sharing, you can operate PC reversely with MAXHUB conference flat panel, or use mobile devices directly operate MAXHUB to write, annotate, present, etc.</li><li style=\"margin-left: 20px;\"><br></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. Ultra-big screen with remote collaboration leads to a boundless office - 12-MP Smart Triple Camera, 8m Voice Picking-up, Screen Sharing, Remote Mirroring, Real Time Writing</span></p></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. Integrated and light assembly</span><br>Built-in camera, voice picking-up, and speaker modules</p></li><li style=\"margin-left: 20px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">. Outstanding remote configuration is specialized for multi-parties HD conference</span><br>Leading technology, applied for presenting more fluent, clear and stable audio and video experiences, includes 12-megapixel smart triple cameras, 6 built-in array microphones, 8m voice picking-up, auditory localization system, 2.1 channel stereo, and real human voice restored by intelligent EQ.</p></li><li style=\"margin-left: 20px;\"><span style=\"font-weight: bolder;\">. Ultra-big screen remote collaboration eliminates the space limitation</span><br>Through remote screen sharing, mirroring and real time writing, you will have HD video and sharing contents on the screen, just like you are working face to face in the same room with your colleagues, partners and clients</li></ul>', '2022-09-20', '', '', 'NGN 3,250,000', '/assets/images/screens/1663679505.075185-2-0,/assets/images/screens/1663679505.0831714-2-1', 2, 1, 'nil', 2, 'Maxhub 75 inches Interactive Display to Enhance Classroom Learning with anti-glare toughness glass, Infrared Touching Tec (20 touch points), 4K panel with 16:9 Format @3840 x 2160 resolution.'),
(2, 'SAMSUNG 43 INCHES SMART SIGNAGE', '<div style=\"color: rgb(104, 113, 136); font-size: 16px;\"><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">Durable premium displays optimize operations and message quality in any environment</span><span style=\"font-weight: bolder;\"></span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsungs TIZEN-powered PMH Series premium displays achieve peak performance all while maintaining a stylish and captivating design. The PMH Series displays leverage elevated brightness and refined image sharpness to ensure a consistently clear presentation even in settings with variable lighting. Additionally, the IP5x-certified PMH Series displays achieve robust, 24/7 durability for dependable and uninterrupted operations. As a result, businesses can feel confident that their messages will be delivered exactly as intended anywhere and at any time</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\"><br></span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\"></span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\"></span><span style=\"font-weight: bolder;\"></span><span style=\"font-weight: bolder;\">Brilliant, Glare-Free Visual Quality</span><span style=\"font-weight: bolder;\"></span><span style=\"font-weight: bolder;\"></span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder; color: rgb(104, 113, 136);\"></span><span style=\"font-weight: bolder; color: rgb(104, 113, 136);\"></span><span style=\"color: rgb(104, 113, 136);\">Equipped with a non-glare frontal panel, the PMH Series displays reduce natural and ambient light interference to ensure continuous readability in any location. Image visibility and information readability are deemed to be very high, because it is less reflective under light or sunlight, which poses no issues when used with QSR menu boards, or airport flight schedule boards with ample natural light.</span></p></div>', '2022-09-20', '', '', 'NGN 485,000', '/assets/images/screens/1663680067.7989616-2-0,/assets/images/screens/1663680067.8049436-2-1,/assets/images/screens/1663680067.8159142-2-2,/assets/images/screens/1663680067.821179-2-3', 1, 2, 'nil', 2, 'Premium TIZEN-powered displays built to handle any business need with 24/7 durability.'),
(3, 'SAMSUNG 32 INCHES MIRROR DISPLAY', '<div style=\"color: rgb(104, 113, 136); font-size: 16px;\"><div><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">A Captivating Mirror/Signage Hybrid Display</span></p></div><div><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s MLE mirror displays create a more engaging and informative customer experience by combining the power and reach of digital signage with the visual clarity of a standard mirror. Featuring high (55 percent) reflectance, the MLE displays clearly portray both real-time mirror imagery and complementary content with minimal visual impairment. Through improved visual accuracy, the MLE mirror display can serve as a valuable sales tool that persuades and informs customers.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><br></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">Clearer, More Visible Presentation</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The unique composition of Samsung’s MLE mirror displays offers consumers a more realistic and complete product view. Featuring a polarized film overlay, the MLE mirror displays deliver superb transmittance (90 percent) and advanced reflectance (55 percent) that reduce visual distraction. As a result, customers can enjoy clearer and more vivid content than standard half-mirror format alternatives offer while simultaneously receiving higher-performing mirror visibility.<br></p><div><br></div><div><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">Distraction-Free Design</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s MLE displays elevate the traditional mirror through a bezel-free design that further keeps viewers focused on reflected and shared content rather than on the signage itself. Additionally, this bezel-free composition grants retail owners added flexibility to take their mirror display arrangements even further. Several MLE displays can be combined into unique, video-wall style arrangements without gaps or inconsistencies between screens, generating endless visual possibilities.<br></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><br></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">Easy Content Control</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Enjoy the versatility of expanded connectivity to mobile devices, from easy media sharing and screen control to simple content mirroring from a tablet or mobile phone to your display. With Samsung MagicInfo content management software, selecting and scheduling software is simple to control with either an RS232 or LAN/WiFi connection.&nbsp;</p></div></div></div>', '2022-09-20', '', '', 'NGN 410,000', '/assets/images/screens/1663680200.669857-2-0,/assets/images/screens/1663680200.6795206-2-1,/assets/images/screens/1663680200.6855028-2-2', 1, 2, 'nil', 1, 'A harmonized hybrid display with integrated digital signage and mirror functionalities.'),
(4, 'VESTEL 32 INCH SCREEN', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">VESTEL 32inch Deluxe Hotel Series</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Vestel 32inch is a Hotel Series Hospitality Display that allow hotels display beautiful contents to engage visitors</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">&nbsp;</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">FEATURES</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Software Deluxe+</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Hybrid Stream (Tuner+IP) Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">&nbsp;Channel List Management Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Supported Tuner Modes DVB-T2/C/S2</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Video Coding HEVC Standalone</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">HTML-based solution Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Smart Channel Listing Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Auto Program Sorting Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">USB Cloning Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Enable/Disable Installation Menus Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Multi IR Code Available Auto TV Off / Auto Sleep Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Anti Theft Battery System Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Wake-up Alarm / Sleep Timer Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">USB Media Player Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Smart TV features Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Smart Center Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Power Save mode (Energy Saving) Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Teletext Available</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Electronic Program Guide EPG Timeline Schedule Energy Saving Available</p>', '2022-09-20', '', '', 'NGN 395,000', '/assets/images/screens/1663680792.1600115-2-0,/assets/images/screens/1663680792.1649947-2-1', 1, 5, 'nil', 2, 'Designed For Hotels'),
(5, 'SAMSUNG 49 INCHES SMART LFD SCREEN', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Premium TIZEN-powered displays built to handle any business need in a slim, captivating design.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">· &nbsp; &nbsp; &nbsp; &nbsp; All-in-one display solution with embedded MagicInfo Player S4 powered by TIZEN™</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">· &nbsp; &nbsp; &nbsp; &nbsp; IP5x certification and non-glare panel to withstand a range of environmental conditions</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">· &nbsp; &nbsp; &nbsp; &nbsp; Sleek design with slim depth (29.9mm) and narrow bezels (6.9mm)</p>', '2022-09-20', '', '', 'NGN 680,000', '/assets/images/screens/1663685624.4890006-2-0,/assets/images/screens/1663685624.4949827-2-1,/assets/images/screens/1663685624.5039463-2-2', 1, 2, 'nil', 1, 'Premium TIZEN-powered displays built to handle any business need in a slim, captivating design.'),
(6, 'VESTEL 55 INCHES SCREEN', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">4 Times Clearer Image 4 Times More Vivid Colors</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Vestel 4K Ultra HD Technology has 4 times higher resolution than Full HD. With its 4 times higher pixel density, it provides more vivid colors, sharpen object shapes, clarify details, and provide a 3D-like experience via image depth.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">INTERNAL HD SATELLITE RECEIVER:</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">In Satellite Broadcasts; Box, Cable, Remote Control is Over!</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">With the internal HD digital satellite receiver, you can receive satellite broadcasts directly without the need for extra equipment. This eliminates the need for extra boxes, controls and cables</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">SMART TV:</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Intelligent, Pleasant, And Rich!</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Beyond a standard television, offering different content alternatives, Vestel Smart TV makes the time at home more enjoyable.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">NETFLIX:</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Thousands of TV shows in your TV with Netflix!</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Thanks to Vestel Smart TV, its easy to watch the most famous movies and the most popular TV shows anymore</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">SMART ADVICE:</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Watch Programs Always You Like on TV!</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The Smart Advice learns your preferences and viewing habits while you are watching television, suggests programs for you, and notifies you of popular programming</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><br></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">SMART GUIDE:</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">No need to worry about which program you will watch tonight!</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Do not waste your whole evening getting lost among hundreds of channels. With the Smart Guide feature, you can easily access the broadcast flow of all channels and program details. This feature is available in the Smart TV application menu, which you can use through the Vestel Smart Center mobile application.</p>', '2022-09-20', '', '', 'NGN 750,000', '/assets/images/screens/1663685717.4958813-2-0,/assets/images/screens/1663685717.4978762-2-1,/assets/images/screens/1663685717.5008667-2-2', 1, 5, 'nil', 1, '4 Times Clearer Image 4 Times More Vivid Colors'),
(7, 'SAMSUNG 32 INCHES TV', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Brand: Samsung<br>Connectivity technology : USB<br>Display technology: LCD<br>Screen size : 32 Inch<br>Refresh rate : 50 Hz<br>Item weight : 4 Kilograms<br>Tuner technology : Mpeg4<br>Model name : HG32EE470<br></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">THE PERFECT SCREENS FOR HOTELS&nbsp;</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung Hotel TV 32EE470SK, energy efficiency class: A+, TV tuner: Analog, DVB-C (cable), DVB-T2 (terrestrial), diagonal screen size: 32 inch, color: Black, resolution: 1366 x 768 (WXGA), HDMI ports: 1, interfaces:...</p>', '2022-09-20', '', '', 'NGN 385,000', '/assets/images/screens/1663685874.9175246-2-0,/assets/images/screens/1663685874.9195194-2-1,/assets/images/screens/1663685874.923509-2-2', 1, 2, 'nil', 1, 'Highly functional, elegant and cost-efficient hospitality displays to enhance guest room ambience'),
(8, 'SAMSUNG 22 INCHES TOUCH SCREEN', '<p><span style=\"color: rgb(104, 113, 136);\">Screen size : 22 Inches</span><br style=\"color: rgb(104, 113, 136);\"><span style=\"color: rgb(104, 113, 136);\">Resolution : FHD 1080p</span><br style=\"color: rgb(104, 113, 136);\"><span style=\"color: rgb(104, 113, 136);\">Display technology : LCD</span><br style=\"color: rgb(104, 113, 136);\"><span style=\"color: rgb(104, 113, 136);\">Brand : Samsung</span><br style=\"color: rgb(104, 113, 136);\"><span style=\"color: rgb(104, 113, 136);\">Series : DB22D-T</span><br style=\"color: rgb(104, 113, 136);\"><br style=\"color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder; color: rgb(104, 113, 136);\">About this item</span><br style=\"color: rgb(104, 113, 136);\"><span style=\"color: rgb(104, 113, 136);\">All-in-One solution thanks to SSP with a quad core processor and Magic Info software</span><br style=\"color: rgb(104, 113, 136);\"><span style=\"color: rgb(104, 113, 136);\">Touchscreen interactivity and a 22\" form factor for small, close placements</span><br style=\"color: rgb(104, 113, 136);\"><span style=\"color: rgb(104, 113, 136);\">Slim 2.3\" chassis depth with slim-direct LED backlight technology</span></p>', '2022-09-20', '', '', 'NGN 550,000', '/assets/images/screens/1663685982.6086679-2-0,/assets/images/screens/1663685982.6106577-2-1,/assets/images/screens/1663685982.6126523-2-2', 1, 2, 'nil', 2, 'An interactive display with an embedded content management solution.'),
(9, 'SAMSUNG 43 INCHES SCREEN', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136); line-height: 28px; font-size: 16px;\"><span style=\"font-weight: bolder;\">displays</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsungs PMF-BC displays combine the visual power of its signage with the touch-driven efficiency of its interactive offerings to better serve the needs of retail, public, corporate and transportation environments, among others.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The displays allow consumers to seamlessly navigate a range of relevant content without interference from surrounding light or environmental conditions.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">Operating System</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The integrated, powerful Tizen operating system grants PMF-BC users exciting capabilities to deliver rich, engaging content with minimal operational burden required.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">Signage Components</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s PMF-BC displays condense several vital signage components – including a powerful operating system, embedded media player and capacitive touch technology – into an all-in-one solution. Backed by the versatile Tizen OS, the PMF-BC displays deliver dynamic, touch-enabled content without requiring external PCs or devices. An intuitive interface further drives quick and convenient navigation across essential applications and content.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">User Convenience</span></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The PMF-BC displays drive user convenience through a centralized infrared receiver (IR). Contrary to standard displays which place their IR in a hard-to-access - and thus hard-to-control - location, the PMF-BC displays receive IR signals across their individual panels. As a result, users can activate IR functionalities from various locations and further augment quick and uninterrupted management.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">&nbsp;</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"><span style=\"font-weight: bolder;\">Screen Size</span>&nbsp;: 43 Inches<br><span style=\"font-weight: bolder;\">Resolution</span>&nbsp;: FHD 1080i<br><span style=\"font-weight: bolder;\">Display Technology</span>&nbsp;: LCD<br><span style=\"font-weight: bolder;\">Brand</span>&nbsp;: SAMSUNG<br><span style=\"font-weight: bolder;\">Aspect Ratio</span>&nbsp;: 16:9<br><span style=\"font-weight: bolder;\">Hardware Interface</span>&nbsp;: USB, HDMI<br><span style=\"font-weight: bolder;\">Refresh Rate</span>&nbsp;: 60<br><span style=\"font-weight: bolder;\">Response Time</span>&nbsp;: 8 Milliseconds<br><span style=\"font-weight: bolder;\">Display Resolution Maximum:</span>&nbsp;1920x1080 Pixels<br><span style=\"font-weight: bolder;\">Total HDMI Ports</span>&nbsp;: 2</p>', '2022-09-20', '', '', 'NGN 950,000', '/assets/images/screens/1663686084.3605165-2-0,/assets/images/screens/1663686084.364405-2-1,/assets/images/screens/1663686084.3673973-2-2', 1, 2, 'nil', 1, 'All-in-one displays that leverage capacitive touch technology backed by Tizen-powered media player.'),
(10, 'SAMSUNG 43 INCHES SMART SIGNAGE VIDEO WALL', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Time to upscale your display</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s new QMR series displays cut through the clutter to deliver best-in-class UHD resolution as well as intelligent UHD upscaling and rich flawless colors with Dynamic Crystal Color all in a slim design.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Incredible 4K picture quality</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s new QMR series provides ultra high-definition 4K resolution, creating lifelike images with sharper picture quality than ever before.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Crystal Processor 4K</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Intelligent UHD upscaling technology, made possibly by Samsung’s Crystal Processor 4K, allows content developed at a lower resolution to be elevated to UHD-level quality. It also performs edge restoration and noise reduction to optimize on-screen text and imagery.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Dynamic Crystal Display</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The QMR series features Dynamic Crystal Display, using 10 bit processing for flawless color expression, allowing viewers to enjoy a wider spectrum of colors up to one billion shades. HDR+ compatibility converts standard definition content to HDR quality for sharper contrast and more vivid colors</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung Workspace secured by Knox</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">With security provided by Knox, the displays feature Samsung Workspace which supports wireless cloud service access and control of a PC without needing a physical connection. Samsung Workspace simplifies meeting spaces while also improving security.</p>', '2022-09-20', '', '', 'NGN 545,000', '/assets/images/screens/1663686184.9564989-2-0,/assets/images/screens/1663686184.9584928-2-1,/assets/images/screens/1663686184.961486-2-2', 1, 2, 'nil', 24, 'SAMSUNG 43 INCHES SMART SIGNAGE VIDEO WALL'),
(11, 'SAMSUNG 49 INCHES SMART SIGNAGE VIDEO WALL', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Time to upscale your display</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s new QMR series displays cut through the clutter to deliver best-in-class UHD resolution as well as intelligent UHD upscaling and rich flawless colors with Dynamic Crystal Color all in a slim design.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Incredible 4K picture quality</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s new QMR series provides ultra high-definition 4K resolution, creating lifelike images with sharper picture quality than ever before.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Crystal Processor 4K</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Intelligent UHD upscaling technology, made possibly by Samsung’s Crystal Processor 4K, allows content developed at a lower resolution to be elevated to UHD-level quality. It also performs edge restoration and noise reduction to optimize on-screen text and imagery.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Dynamic Crystal Display</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The QMR series features Dynamic Crystal Display, using 10 bit processing for flawless color expression, allowing viewers to enjoy a wider spectrum of colors up to one billion shades. HDR+ compatibility converts standard definition content to HDR quality for sharper contrast and more vivid colors</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung Workspace secured by Knox</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">With security provided by Knox, the displays feature Samsung Workspace which supports wireless cloud service access and control of a PC without needing a physical connection. Samsung Workspace simplifies meeting spaces while also improving security.</p>', '2022-09-20', '', '', 'NGN 810,000', '/assets/images/screens/1663686365.5782444-2-0,/assets/images/screens/1663686365.583104-2-1,/assets/images/screens/1663686365.5855663-2-2', 1, 2, 'nil', 12, 'Display any content in ultra-high definition with incredibly rich color on slim, efficient signage.'),
(12, 'SAMSUNG 65 INCHES SMART SIGNAGE VIDEO WALL', '<p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Time to upscale your display<br></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s new QBR series displays cut through the clutter to deliver best-in-class UHD resolution as well as intelligent UHD upscaling and rich flawless colors with Dynamic Crystal Color all in a slim design.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Incredible 4K picture quality</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung’s new QBR series provides ultra-high-definition 4K resolution, creating lifelike images with sharper picture quality than ever before.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Crystal Processor 4K</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Intelligent UHD upscaling technology, made possibly by Samsung’s Crystal Processor 4K, allows content developed at a lower resolution to be elevated to UHD-level quality. It also performs edge restoration and noise reduction to optimize on-screen text and imagery.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Slim and symmetrical design</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The QBR series features an all-new symmetric design simplifying wall mounting and ensuring installation is seamless. The flat back and slim depth will ensure a display that will stand the test of time.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Clean cable management</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">With QBRs new cable guide feature, retailers are able to tuck away messy cables from view. This allows for a clean and visually-appealing shopping expeience for customers, even when the back of the display is visible.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Powerful, all-in-one solution</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">SSSP is an all-in-one solution that simplifies installation and maintenance. With Tizen 4.0, businesses can enjoy easy development, reinforced capability with multiple web formats and standards and secured protection.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Samsung Workspace secured by Knox</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">With security provided by Knox, the displays feature Samsung Workspace which supports wireless cloud service access and control of a PC without needing a physical connection. Samsung Workspace simplifies meeting spaces while also improving security.</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\"></p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">Industry standard certified</p><p style=\"margin-top: 0px; margin-bottom: 25px; color: rgb(104, 113, 136);\">The QBR series guarantees dependable functionality and is environmentally sustainable. Electromagnetic compatibility (EMC) class B compliant, meeting strict safety and reliability standards for operation, the displays are also registered by EPEAT, the global ecolabel for IT.</p>', '2022-09-20', '', '', 'NGN 890,000', '/assets/images/screens/1663686533.851193-2-0,/assets/images/screens/1663686533.854187-2-1,/assets/images/screens/1663686533.8561823-2-2', 1, 2, 'nil', 3, 'Display any content in ultra-high definition with incredibly rich color on slim, efficient signage');

-- --------------------------------------------------------

--
-- Table structure for table `screens_bookings`
--

CREATE TABLE `screens_bookings` (
  `id` int(255) NOT NULL,
  `user_id` int(255) NOT NULL,
  `screen_id` int(255) NOT NULL,
  `date_added` date NOT NULL,
  `date_for_pickup` date NOT NULL,
  `date_for_return` date NOT NULL,
  `added_by` text NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `screens_bookings`
--

INSERT INTO `screens_bookings` (`id`, `user_id`, `screen_id`, `date_added`, `date_for_pickup`, `date_for_return`, `added_by`, `status`) VALUES
(1, 1, 1, '2022-09-20', '2022-09-21', '2022-10-07', '', 'Pending'),
(3, 1, 2, '2022-09-20', '2022-09-23', '2022-10-04', '', 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `subscribed_emails`
--

CREATE TABLE `subscribed_emails` (
  `id` int(255) NOT NULL,
  `email` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(255) NOT NULL,
  `firstname` text NOT NULL,
  `lastname` text NOT NULL,
  `email` longtext NOT NULL,
  `password` longtext NOT NULL,
  `status` text NOT NULL,
  `profile_picture` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `password`, `status`, `profile_picture`) VALUES
(1, 'benjamin', 'ikirigbe', 'diaphorosnachalah77@gmail.com', '11111111', 'active', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `brandd`
--
ALTER TABLE `brandd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `categoryy`
--
ALTER TABLE `categoryy`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `screenss`
--
ALTER TABLE `screenss`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `screens_bookings`
--
ALTER TABLE `screens_bookings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subscribed_emails`
--
ALTER TABLE `subscribed_emails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `brandd`
--
ALTER TABLE `brandd`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `categoryy`
--
ALTER TABLE `categoryy`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `screenss`
--
ALTER TABLE `screenss`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `screens_bookings`
--
ALTER TABLE `screens_bookings`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `subscribed_emails`
--
ALTER TABLE `subscribed_emails`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
