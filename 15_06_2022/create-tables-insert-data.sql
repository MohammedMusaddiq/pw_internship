create table pw_assignment.customer
(
    customer_id   int auto_increment
        primary key,
    customer_name varchar(50) not null
);

INSERT INTO pw_assignment.customer (customer_id, customer_name)
VALUES (1, 'John');
INSERT INTO pw_assignment.customer (customer_id, customer_name)
VALUES (2, 'Smith');
INSERT INTO pw_assignment.customer (customer_id, customer_name)
VALUES (3, 'Ricky');
INSERT INTO pw_assignment.customer (customer_id, customer_name)
VALUES (4, 'Walsh');
INSERT INTO pw_assignment.customer (customer_id, customer_name)
VALUES (5, 'Stefen');
INSERT INTO pw_assignment.customer (customer_id, customer_name)
VALUES (6, 'Fleming');
INSERT INTO pw_assignment.customer (customer_id, customer_name)
VALUES (7, 'Thomson');
INSERT INTO pw_assignment.customer (customer_id, customer_name)
VALUES (8, 'David');


create table pw_assignment.product
(
    product_id    int auto_increment
        primary key,
    product_name  varchar(50) not null,
    product_price int         not null
);

INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (1, 'Television', 19000);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (2, 'DVD', 3600);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (3, 'Washing Machine', 7600);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (4, 'Computer', 35900);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (5, 'Ipod', 3210);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (6, 'Panasonic Phone', 2100);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (7, 'Chair', 360);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (8, 'Table', 490);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (9, 'Sound System', 12050);
INSERT INTO pw_assignment.product (product_id, product_name, product_price)
VALUES (10, 'Home Theatre', 19350);


create table pw_assignment.order
(
    order_id    tinyint auto_increment
        primary key,
    customer_id int  not null,
    order_date  date not null,
    constraint order_customer_customer_id_fk
        foreign key (customer_id) references pw_assignment.customer (customer_id)
);

INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (1, 4, '2005-01-05');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (2, 2, '2006-02-10');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (3, 3, '2005-03-20');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (4, 3, '2006-03-10');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (5, 1, '2007-04-05');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (6, 7, '2006-12-13');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (7, 6, '2008-03-13');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (8, 6, '2004-11-29');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (9, 5, '2005-01-13');
INSERT INTO pw_assignment.`order` (order_id, customer_id, order_date)
VALUES (10, 1, '2007-12-12');


create table pw_assignment.order_details
(
    order_details_id int auto_increment
        primary key,
    order_id         tinyint not null,
    product_id       int null,
    quantity         int null,
    constraint order_details_order_order_id_fk
        foreign key (order_id) references pw_assignment.`order` (order_id)
            on update cascade,
    constraint order_details_product_product_id_fk
        foreign key (product_id) references pw_assignment.product (product_id)
            on update cascade
);

INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (4, 1, 3, 1);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (5, 1, 2, 3);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (6, 2, 10, 2);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (7, 3, 7, 10);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (8, 3, 4, 2);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (9, 3, 5, 4);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (10, 4, 3, 1);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (11, 5, 1, 2);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (12, 5, 2, 1);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (13, 6, 5, 1);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (14, 7, 6, 1);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (15, 8, 10, 2);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (16, 8, 3, 1);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (17, 9, 10, 3);
INSERT INTO pw_assignment.order_details (order_details_id, order_id, product_id, quantity)
VALUES (18, 10, 1, 1);






