# ----- Imports --------------------------------------------------------------

from tinyAPI.base.config import ConfigManager

import tinyAPI

# ----- Instructions ---------------------------------------------------------

def geo_build():
    db = ConfigManager.value('default schema')
    if db is None:
        return []

    return [
        tinyAPI.RefTable(db, 'geo_ref_continent')
            .add(1, 'Africa')
            .add(2, 'Antarctica')
            .add(3, 'Asia')
            .add(4, 'Australia')
            .add(5, 'Europe')
            .add(6, 'North America')
            .add(7, 'South America'),

        tinyAPI.RefTable(db, 'geo_ref_us_region')
            .add(1, 'Northeast')
            .add(2, 'Southeast')
            .add(3, 'Midwest')
            .add(4, 'Southwest')
            .add(5, 'West'),

        tinyAPI.Table(db, 'geo_country')
            .serial()
            .vchar('name', 100, True)
            .char('iso_3166_code', 2, True)
            .id('continent_id')
                .fk('geo_ref_continent')
            .idx(['continent_id'])
            .ins(1, 'Afghanistan', 'AF', 3)
            .ins(2, 'Aland Islands', 'AX', 5)
            .ins(3, 'Albania', 'AL', 5)
            .ins(4, 'Algeria', 'DZ', 1)
            .ins(5, 'American Samoa', 'AS', 6)
            .ins(6, 'Andorra', 'AD', 5)
            .ins(7, 'Angola', 'AO', 1)
            .ins(8, 'Anguilla', 'AI', 6)
            .ins(9, 'Antarctica', 'AQ', 2)
            .ins(10, 'Antigua And Barbuda', 'AG', 6)
            .ins(11, 'Argentina', 'AR', 7)
            .ins(12, 'Armenia', 'AM', 3)
            .ins(13, 'Aruba', 'AW', 6)
            .ins(14, 'Australia', 'AU', 4)
            .ins(15, 'Austria', 'AT', 5)
            .ins(16, 'Azerbaijan', 'AZ', 3)
            .ins(17, 'Bahamas', 'BS', 6)
            .ins(18, 'Bahrain', 'BH', 3)
            .ins(19, 'Bangladesh', 'BD', 3)
            .ins(20, 'Barbados', 'BB', 6)
            .ins(21, 'Belarus', 'BY', 5)
            .ins(22, 'Belgium', 'BE', 5)
            .ins(23, 'Belize', 'BZ', 6)
            .ins(24, 'Benin', 'BJ', 1)
            .ins(25, 'Bermuda', 'BM', 6)
            .ins(26, 'Bhutan', 'BT', 3)
            .ins(27, 'Bolivia', 'BO', 7)
            .ins(28, 'Bosnia And Herzegovina', 'BA', 4)
            .ins(29, 'Botswana', 'BW', 1)
            .ins(30, 'Bouvet Island', 'BV', 2)
            .ins(31, 'Brazil', 'BR', 7)
            .ins(32, 'British Indian Ocean Territory', 'IO', 3)
            .ins(33, 'Brunei Darussalam', 'BN', 3)
            .ins(34, 'Bulgaria', 'BG', 5)
            .ins(35, 'Burkina Faso', 'BF', 1)
            .ins(36, 'Burundi', 'BI', 1)
            .ins(37, 'Cambodia', 'KH', 3)
            .ins(38, 'Cameroon', 'CM', 1)
            .ins(39, 'Canada', 'CA', 6)
            .ins(40, 'Cape Verde', 'CV', 1)
            .ins(41, 'Cayman Islands', 'KY', 6)
            .ins(42, 'Central African Republic', 'CF', 1)
            .ins(43, 'Chad', 'TD', 1)
            .ins(44, 'Chile', 'CL', 7)
            .ins(45, 'China', 'CN', 3)
            .ins(46, 'Christmas Island', 'CX', 3)
            .ins(47, 'Cocos (keeling) Islands', 'CC', 3)
            .ins(48, 'Colombia', 'CO', 7)
            .ins(49, 'Comoros', 'KM', 1)
            .ins(50, 'Congo', 'CG', 1)
            .ins(51, 'Congo, The Democratic Republic Of The', 'CD', 1)
            .ins(52, 'Cook Islands', 'CK', 4)
            .ins(53, 'Costa Rica', 'CR', 6)
            .ins(54, 'Cote D''ivoire', 'CI', 1)
            .ins(55, 'Croatia', 'HR', 5)
            .ins(56, 'Cuba', 'CU', 6)
            .ins(57, 'Cyprus', 'CY', 3)
            .ins(58, 'Czech Republic', 'CZ', 5)
            .ins(59, 'Denmark', 'DK', 5)
            .ins(60, 'Djibouti', 'DJ', 1)
            .ins(61, 'Dominica', 'DM', 6)
            .ins(62, 'Dominican Republic', 'DO', 6)
            .ins(63, 'Ecuador', 'EC', 7)
            .ins(64, 'Egypt', 'EG', 1)
            .ins(65, 'El Salvador', 'SV', 6)
            .ins(66, 'Equatorial Guinea', 'GQ', 1)
            .ins(67, 'Eritrea', 'ER', 1)
            .ins(68, 'Estonia', 'EE', 5)
            .ins(69, 'Ethiopia', 'ET', 1)
            .ins(70, 'Falkland Islands (malvinas)', 'FK', 7)
            .ins(71, 'Faroe Islands', 'FO', 5)
            .ins(72, 'Fiji', 'FJ', 4)
            .ins(73, 'Finland', 'FI', 5)
            .ins(74, 'France', 'FR', 5)
            .ins(75, 'French Guiana', 'GF', 7)
            .ins(76, 'French Polynesia', 'PF', 4)
            .ins(77, 'French Southern Territories', 'TF', 2)
            .ins(78, 'Gabon', 'GA', 1)
            .ins(79, 'Gambia', 'GM', 1)
            .ins(80, 'Georgia', 'GE', 3)
            .ins(81, 'Germany', 'DE', 5)
            .ins(82, 'Ghana', 'GH', 1)
            .ins(83, 'Gibraltar', 'GI', 5)
            .ins(84, 'Greece', 'GR', 5)
            .ins(85, 'Greenland', 'GL', 6)
            .ins(86, 'Grenada', 'GD', 6)
            .ins(87, 'Guadeloupe', 'GP', 6)
            .ins(88, 'Guam', 'GU', 4)
            .ins(89, 'Guatemala', 'GT', 6)
            .ins(90, 'Guernsey', 'GG', 5)
            .ins(91, 'Guinea', 'GN', 1)
            .ins(92, 'Guinea-bissau', 'GW', 1)
            .ins(93, 'Guyana', 'GY', 7)
            .ins(94, 'Haiti', 'HT', 6)
            .ins(95, 'Heard Island And Mcdonald Islands', 'HM', 2)
            .ins(96, 'Holy See', 'VA', 5)
            .ins(97, 'Honduras', 'HN', 6)
            .ins(98, 'Hong Kong', 'HK', 3)
            .ins(99, 'Hungary', 'HU', 5)
            .ins(100, 'Iceland', 'IS', 5)
            .ins(101, 'India', 'IN', 3)
            .ins(102, 'Indonesia', 'ID', 3)
            .ins(103, 'Iran, Islamic Republic Of', 'IR', 3)
            .ins(104, 'Iraq', 'IQ', 3)
            .ins(105, 'Ireland', 'IE', 5)
            .ins(106, 'Isle Of Man', 'IM', 5)
            .ins(107, 'Israel', 'IL', 3)
            .ins(108, 'Italy', 'IT', 5)
            .ins(109, 'Jamaica', 'JM', 6)
            .ins(110, 'Japan', 'JP', 3)
            .ins(111, 'Jersey', 'JE', 5)
            .ins(112, 'Jordan', 'JO', 3)
            .ins(113, 'Kazakhstan', 'KZ', 3)
            .ins(114, 'Kenya', 'KE', 1)
            .ins(115, 'Kiribati', 'KI', 4)
            .ins(116, 'Korea, Democratic People''s Republic Of', 'KP', 3)
            .ins(117, 'Korea, Republic Of', 'KR', 3)
            .ins(118, 'Kuwait', 'KW', 3)
            .ins(119, 'Kyrgyzstan', 'KG', 3)
            .ins(120, 'Lao People''s Democratic Republic', 'LA', 3)
            .ins(121, 'Latvia', 'LV', 5)
            .ins(122, 'Lebanon', 'LB', 3)
            .ins(123, 'Lesotho', 'LS', 1)
            .ins(124, 'Liberia', 'LR', 1)
            .ins(125, 'Libyan Arab Jamahiriya', 'LY', 1)
            .ins(126, 'Liechtenstein', 'LI', 5)
            .ins(127, 'Lithuania', 'LT', 5)
            .ins(128, 'Luxembourg', 'LU', 5)
            .ins(129, 'Macao', 'MO', 3)
            .ins(130, 'Macedonia, The Former Yugoslav Republic Of', 'MK', 5)
            .ins(131, 'Madagascar', 'MG', 1)
            .ins(132, 'Malawi', 'MW', 1)
            .ins(133, 'Malaysia', 'MY', 3)
            .ins(134, 'Maldives', 'MV', 3)
            .ins(135, 'Mali', 'ML', 1)
            .ins(136, 'Malta', 'MT', 5)
            .ins(137, 'Marshall Islands', 'MH', 4)
            .ins(138, 'Martinique', 'MQ', 6)
            .ins(139, 'Mauritania', 'MR', 1)
            .ins(140, 'Mauritius', 'MU', 1)
            .ins(141, 'Mayotte', 'YT', 1)
            .ins(142, 'Mexico', 'MX', 6)
            .ins(143, 'Micronesia, Federated States Of', 'FM', 4)
            .ins(144, 'Moldova', 'MD', 5)
            .ins(145, 'Monaco', 'MC', 5)
            .ins(146, 'Mongolia', 'MN', 3)
            .ins(147, 'Montenegro', 'ME', 5)
            .ins(148, 'Montserrat', 'MS', 6)
            .ins(149, 'Morocco', 'MA', 1)
            .ins(150, 'Mozambique', 'MZ', 1)
            .ins(151, 'Myanmar', 'MM', 3)
            .ins(152, 'Namibia', 'NA', 1)
            .ins(153, 'Nauru', 'NR', 4)
            .ins(154, 'Nepal', 'NP', 3)
            .ins(155, 'Netherlands', 'NL', 5)
            .ins(156, 'Netherlands Antilles', 'AN', 6)
            .ins(157, 'New Caledonia', 'NC', 4)
            .ins(158, 'New Zealand', 'NZ', 4)
            .ins(159, 'Nicaragua', 'NI', 6)
            .ins(160, 'Niger', 'NE', 1)
            .ins(161, 'Nigeria', 'NG', 1)
            .ins(162, 'Niue', 'NU', 4)
            .ins(163, 'Norfolk Island', 'NF', 4)
            .ins(164, 'Northern Mariana Islands', 'MP', 4)
            .ins(165, 'Norway', 'NO', 5)
            .ins(166, 'Oman', 'OM', 3)
            .ins(167, 'Pakistan', 'PK', 3)
            .ins(168, 'Palau', 'PW', 4)
            .ins(169, 'Palestinian Territory, Occupied', 'PS', 3)
            .ins(170, 'Panama', 'PA', 6)
            .ins(171, 'Papua New Guinea', 'PG', 4)
            .ins(172, 'Paraguay', 'PY', 7)
            .ins(173, 'Peru', 'PE', 7)
            .ins(174, 'Philippines', 'PH', 3)
            .ins(175, 'Pitcairn', 'PN', 4)
            .ins(176, 'Poland', 'PL', 5)
            .ins(177, 'Portugal', 'PT', 5)
            .ins(178, 'Puerto Rico', 'PR', 6)
            .ins(179, 'Qatar', 'QA', 3)
            .ins(180, 'Reunion', 'RE', 1)
            .ins(181, 'Romania', 'RO', 5)
            .ins(182, 'Russian Federation', 'RU', 3)
            .ins(183, 'Rwanda', 'RW', 1)
            .ins(184, 'Saint Barthelemy', 'BL', 6)
            .ins(185, 'Saint Helena', 'SH', 1)
            .ins(186, 'Saint Kitts And Nevis', 'KN', 6)
            .ins(187, 'Saint Lucia', 'LC', 6)
            .ins(188, 'Saint Martin', 'MF', 6)
            .ins(189, 'Saint Pierre And Miquelon', 'PM', 6)
            .ins(190, 'Saint Vincent And The Grenadines', 'VC', 6)
            .ins(191, 'Samoa', 'WS', 4)
            .ins(192, 'San Marino', 'SM', 5)
            .ins(193, 'Sao Tome And Principe', 'ST', 1)
            .ins(194, 'Saudi Arabia', 'SA', 3)
            .ins(195, 'Senegal', 'SN', 1)
            .ins(196, 'Serbia', 'RS', 3)
            .ins(197, 'Seychelles', 'SC', 1)
            .ins(198, 'Sierra Leone', 'SL', 1)
            .ins(199, 'Singapore', 'SG', 3)
            .ins(200, 'Slovakia', 'SK', 5)
            .ins(201, 'Slovenia', 'SI', 5)
            .ins(202, 'Solomon Islands', 'SB', 4)
            .ins(203, 'Somalia', 'SO', 1)
            .ins(204, 'South Africa', 'ZA', 1)
            .ins(205, 'South Georgia And The South Sandwich Islands', 'GS', 4)
            .ins(206, 'Spain', 'ES', 5)
            .ins(207, 'Sri Lanka', 'LK', 3)
            .ins(208, 'Sudan', 'SD', 1)
            .ins(209, 'Suriname', 'SR', 7)
            .ins(210, 'Svalbard And Jan Mayen', 'SJ', 5)
            .ins(211, 'Swaziland', 'SZ', 1)
            .ins(212, 'Sweden', 'SE', 5)
            .ins(213, 'Switzerland', 'CH', 5)
            .ins(214, 'Syrian Arab Republic', 'SY', 3)
            .ins(215, 'Taiwan, Province Of China', 'TW', 3)
            .ins(216, 'Tajikistan', 'TJ', 3)
            .ins(217, 'Tanzania, United Republic Of', 'TZ', 1)
            .ins(218, 'Thailand', 'TH', 3)
            .ins(219, 'Timor-leste', 'TL', 3)
            .ins(220, 'Togo', 'TG', 1)
            .ins(221, 'Tokelau', 'TK', 4)
            .ins(222, 'Tonga', 'TO', 4)
            .ins(223, 'Trinidad And Tobago', 'TT', 6)
            .ins(224, 'Tunisia', 'TN', 1)
            .ins(225, 'Turkey', 'TR', 3)
            .ins(226, 'Turkmenistan', 'TM', 3)
            .ins(227, 'Turks And Caicos Islands', 'TC', 6)
            .ins(228, 'Tuvalu', 'TV', 4)
            .ins(229, 'Uganda', 'UG', 1)
            .ins(230, 'Ukraine', 'UA', 5)
            .ins(231, 'United Arab Emirates', 'AE', 3)
            .ins(232, 'United Kingdom', 'GB', 5)
            .ins(233, 'United States', 'US', 6)
            .ins(234, 'United States Minor Outlying Islands', 'UM', 6)
            .ins(235, 'Uruguay', 'UY', 7)
            .ins(236, 'Uzbekistan', 'UZ', 3)
            .ins(237, 'Vanuatu', 'VU', 4)
            .ins(238, 'Venezuela', 'VE', 7)
            .ins(239, 'Viet Nam', 'VN', 3)
            .ins(241, 'Virgin Islands, U.s.', 'VI', 6)
            .ins(242, 'Wallis And Futuna', 'WF', 4)
            .ins(243, 'Western Sahara', 'EH', 1)
            .ins(244, 'Yemen', 'YE', 3)
            .ins(245, 'Zambia', 'ZM', 1)
            .ins(246, 'Zimbabwe', 'ZW', 1)
            .ins(247, 'Zaire', 'ZR', 1)
            .ins(248, 'Kosovo', 'XK', 5),

        tinyAPI.Table(db, 'geo_us_state')
            .id('us_region_id')
                .fk('geo_ref_us_region')
            .id('id', True, True)
            .char('abbreviation', 2, True)
            .pk(['us_region_id', 'id'])
            .ins(5, 1, 'AK')
            .ins(2, 2, 'AL')
            .ins(2, 3, 'AR')
            .ins(5, 4, 'AS')
            .ins(4, 5, 'AZ')
            .ins(5, 6, 'CA')
            .ins(5, 7, 'CO')
            .ins(1, 8, 'CT')
            .ins(1, 9, 'DC')
            .ins(1, 10, 'DE')
            .ins(2, 11, 'FL')
            .ins(5, 12, 'FM')
            .ins(2, 13, 'GA')
            .ins(5, 14, 'GU')
            .ins(5, 15, 'HI')
            .ins(3, 16, 'IA')
            .ins(5, 17, 'ID')
            .ins(3, 18, 'IL')
            .ins(3, 19, 'IN')
            .ins(3, 20, 'KS')
            .ins(2, 21, 'KY')
            .ins(2, 22, 'LA')
            .ins(1, 23, 'MA')
            .ins(1, 24, 'MD')
            .ins(1, 25, 'ME')
            .ins(5, 26, 'MH')
            .ins(3, 27, 'MI')
            .ins(3, 28, 'MN')
            .ins(3, 29, 'MO')
            .ins(5, 30, 'MP')
            .ins(2, 31, 'MS')
            .ins(5, 32, 'MT')
            .ins(2, 33, 'NC')
            .ins(3, 34, 'ND')
            .ins(3, 35, 'NE')
            .ins(1, 36, 'NH')
            .ins(1, 37, 'NJ')
            .ins(4, 38, 'NM')
            .ins(5, 39, 'NV')
            .ins(1, 40, 'NY')
            .ins(3, 41, 'OH')
            .ins(4, 42, 'OK')
            .ins(5, 43, 'OR')
            .ins(1, 44, 'PA')
            .ins(2, 45, 'PR')
            .ins(5, 46, 'PW')
            .ins(1, 47, 'RI')
            .ins(2, 48, 'SC')
            .ins(3, 49, 'SD')
            .ins(2, 50, 'TN')
            .ins(4, 51, 'TX')
            .ins(5, 52, 'UT')
            .ins(2, 53, 'VA')
            .ins(2, 54, 'VI')
            .ins(1, 55, 'VT')
            .ins(5, 56, 'WA')
            .ins(3, 57, 'WI')
            .ins(2, 58, 'WV')
            .ins(5, 59, 'WY'),

        tinyAPI.Table(db, 'geo_country_code')
            .serial()
            .vchar('country_name', 200, True)
            .vchar('code', 10, True)
            .uk(['country_name', 'code'])
            .ins(1, 'United States', '1')
            .ins(2, 'Afghanistan', '93')
            .ins(3, 'Albania', '355')
            .ins(4, 'Algeria', '213')
            .ins(5, 'Andorra', '376')
            .ins(6, 'Angola', '244')
            .ins(7, 'Antarctica', '672')
            .ins(8, 'Argentina', '54')
            .ins(9, 'Armenia', '374')
            .ins(10, 'Aruba', '297')
            .ins(11, 'Australia', '61')
            .ins(12, 'Austria', '43')
            .ins(13, 'Azerbaijan', '994')
            .ins(14, 'Bahrain', '973')
            .ins(15, 'Bangladesh', '880')
            .ins(16, 'Belarus', '375')
            .ins(17, 'Belgium', '32')
            .ins(18, 'Belize', '501')
            .ins(19, 'Benin', '229')
            .ins(20, 'Bhutan', '975')
            .ins(21, 'Bolivia', '591')
            .ins(22, 'Bosnia and Herzegovina', '387')
            .ins(23, 'Botswana', '267')
            .ins(24, 'Brazil', '55')
            .ins(25, 'British Indian Ocean Territory', '246')
            .ins(26, 'Brunei', '673')
            .ins(27, 'Bulgaria', '359')
            .ins(28, 'Burkina Faso', '226')
            .ins(29, 'Burundi', '257')
            .ins(30, 'Cambodia', '855')
            .ins(31, 'Cameroon', '237')
            .ins(32, 'Canada', '1')
            .ins(33, 'Cape Verde', '238')
            .ins(34, 'Central African Republic', '236')
            .ins(35, 'Chad', '235')
            .ins(36, 'Chile', '56')
            .ins(37, 'China', '86')
            .ins(38, 'Christmas Island', '61')
            .ins(39, 'Cocos Islands', '61')
            .ins(40, 'Colombia', '57')
            .ins(41, 'Comoros', '269')
            .ins(42, 'Cook Islands', '682')
            .ins(43, 'Costa Rica', '506')
            .ins(44, 'Croatia', '385')
            .ins(45, 'Cuba', '53')
            .ins(46, 'Curacao', '599')
            .ins(47, 'Cyprus', '357')
            .ins(48, 'Czech Republic', '420')
            .ins(49, 'Democratic Republic of the Congo', '243')
            .ins(50, 'Denmark', '45')
            .ins(51, 'Djibouti', '253')
            .ins(52, 'East Timor', '670')
            .ins(53, 'Ecuador', '593')
            .ins(54, 'Egypt', '20')
            .ins(55, 'El Salvador', '503')
            .ins(56, 'Equatorial Guinea', '240')
            .ins(57, 'Eritrea', '291')
            .ins(58, 'Estonia', '372')
            .ins(59, 'Ethiopia', '251')
            .ins(60, 'Falkland Islands', '500')
            .ins(61, 'Faroe Islands', '298')
            .ins(62, 'Fiji', '679')
            .ins(63, 'Finland', '358')
            .ins(64, 'France', '33')
            .ins(65, 'French Polynesia', '689')
            .ins(66, 'Gabon', '241')
            .ins(67, 'Gambia', '220')
            .ins(68, 'Georgia', '995')
            .ins(69, 'Germany', '49')
            .ins(70, 'Ghana', '233')
            .ins(71, 'Gibraltar', '350')
            .ins(72, 'Greece', '30')
            .ins(73, 'Greenland', '299')
            .ins(74, 'Guatemala', '502')
            .ins(75, 'Guinea', '224')
            .ins(76, 'Guinea-Bissau', '245')
            .ins(77, 'Guyana', '592')
            .ins(78, 'Haiti', '509')
            .ins(79, 'Honduras', '504')
            .ins(80, 'Hong Kong', '852')
            .ins(81, 'Hungary', '36')
            .ins(82, 'Iceland', '354')
            .ins(83, 'India', '91')
            .ins(84, 'Indonesia', '62')
            .ins(85, 'Iran', '98')
            .ins(86, 'Iraq', '964')
            .ins(87, 'Ireland', '353')
            .ins(88, 'Israel', '972')
            .ins(89, 'Italy', '39')
            .ins(90, 'Ivory Coast', '225')
            .ins(91, 'Japan', '81')
            .ins(92, 'Jordan', '962')
            .ins(93, 'Kazakhstan', '7')
            .ins(94, 'Kenya', '254')
            .ins(95, 'Kiribati', '686')
            .ins(96, 'Kosovo', '383')
            .ins(97, 'Kuwait', '965')
            .ins(98, 'Kyrgyzstan', '996')
            .ins(99, 'Laos', '856')
            .ins(100, 'Latvia', '371')
            .ins(101, 'Lebanon', '961')
            .ins(102, 'Lesotho', '266')
            .ins(103, 'Liberia', '231')
            .ins(104, 'Libya', '218')
            .ins(105, 'Liechtenstein', '423')
            .ins(106, 'Lithuania', '370')
            .ins(107, 'Luxembourg', '352')
            .ins(108, 'Macao', '853')
            .ins(109, 'Macedonia', '389')
            .ins(110, 'Madagascar', '261')
            .ins(111, 'Malawi', '265')
            .ins(112, 'Malaysia', '60')
            .ins(113, 'Maldives', '960')
            .ins(114, 'Mali', '223')
            .ins(115, 'Malta', '356')
            .ins(116, 'Marshall Islands', '692')
            .ins(117, 'Mauritania', '222')
            .ins(118, 'Mauritius', '230')
            .ins(119, 'Mayotte', '262')
            .ins(120, 'Mexico', '52')
            .ins(121, 'Micronesia', '691')
            .ins(122, 'Moldova', '373')
            .ins(123, 'Monaco', '377')
            .ins(124, 'Mongolia', '976')
            .ins(125, 'Montenegro', '382')
            .ins(126, 'Morocco', '212')
            .ins(127, 'Mozambique', '258')
            .ins(128, 'Myanmar', '95')
            .ins(129, 'Namibia', '264')
            .ins(130, 'Nauru', '674')
            .ins(131, 'Nepal', '977')
            .ins(132, 'Netherlands', '31')
            .ins(133, 'Netherlands Antilles', '599')
            .ins(134, 'New Caledonia', '687')
            .ins(135, 'New Zealand', '64')
            .ins(136, 'Nicaragua', '505')
            .ins(137, 'Niger', '227')
            .ins(138, 'Nigeria', '234')
            .ins(139, 'Niue', '683')
            .ins(140, 'North Korea', '850')
            .ins(141, 'Norway', '47')
            .ins(142, 'Oman', '968')
            .ins(143, 'Pakistan', '92')
            .ins(144, 'Palau', '680')
            .ins(145, 'Palestine', '970')
            .ins(146, 'Panama', '507')
            .ins(147, 'Papua New Guinea', '675')
            .ins(148, 'Paraguay', '595')
            .ins(149, 'Peru', '51')
            .ins(150, 'Philippines', '63')
            .ins(151, 'Pitcairn', '64')
            .ins(152, 'Poland', '48')
            .ins(153, 'Portugal', '351')
            .ins(154, 'Qatar', '974')
            .ins(155, 'Republic of the Congo', '242')
            .ins(156, 'Reunion', '262')
            .ins(157, 'Romania', '40')
            .ins(158, 'Russia', '7')
            .ins(159, 'Rwanda', '250')
            .ins(160, 'Saint Barthelemy', '590')
            .ins(161, 'Saint Helena', '290')
            .ins(162, 'Saint Martin', '590')
            .ins(163, 'Saint Pierre and Miquelon', '508')
            .ins(164, 'Samoa', '685')
            .ins(165, 'San Marino', '378')
            .ins(166, 'Sao Tome and Principe', '239')
            .ins(167, 'Saudi Arabia', '966')
            .ins(168, 'Senegal', '221')
            .ins(169, 'Serbia', '381')
            .ins(170, 'Seychelles', '248')
            .ins(171, 'Sierra Leone', '232')
            .ins(172, 'Singapore', '65')
            .ins(173, 'Slovakia', '421')
            .ins(174, 'Slovenia', '386')
            .ins(175, 'Solomon Islands', '677')
            .ins(176, 'Somalia', '252')
            .ins(177, 'South Africa', '27')
            .ins(178, 'South Korea', '82')
            .ins(179, 'South Sudan', '211')
            .ins(180, 'Spain', '34')
            .ins(181, 'Sri Lanka', '94')
            .ins(182, 'Sudan', '249')
            .ins(183, 'Suriname', '597')
            .ins(184, 'Svalbard and Jan Mayen', '47')
            .ins(185, 'Swaziland', '268')
            .ins(186, 'Sweden', '46')
            .ins(187, 'Switzerland', '41')
            .ins(188, 'Syria', '963')
            .ins(189, 'Taiwan', '886')
            .ins(190, 'Tajikistan', '992')
            .ins(191, 'Tanzania', '255')
            .ins(192, 'Thailand', '66')
            .ins(193, 'Togo', '228')
            .ins(194, 'Tokelau', '690')
            .ins(195, 'Tonga', '676')
            .ins(196, 'Tunisia', '216')
            .ins(197, 'Turkey', '90')
            .ins(198, 'Turkmenistan', '993')
            .ins(199, 'Tuvalu', '688')
            .ins(200, 'Uganda', '256')
            .ins(201, 'Ukraine', '380')
            .ins(202, 'United Arab Emirates', '971')
            .ins(203, 'United Kingdom', '44')
            .ins(204, 'Uruguay', '598')
            .ins(205, 'Uzbekistan', '998')
            .ins(206, 'Vanuatu', '678')
            .ins(207, 'Vatican', '379')
            .ins(208, 'Venezuela', '58')
            .ins(209, 'Vietnam', '84')
            .ins(210, 'Wallis and Futuna', '681')
            .ins(211, 'Western Sahara', '212')
            .ins(212, 'Yemen', '967')
            .ins(213, 'Zambia', '260')
            .ins(214, 'Zimbabwe', '263')
    ]
