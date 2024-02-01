create database UFC;
use UFC;




-- create table RED_CORNER (
--	age integer,
--	weight float,
--	win_streak integer,
--	wins integer,
--	losses integer,
--	draws integer,
--    fight_id integer,
--    fighter_code integer,
--    foreign key (fight_id)
--    references FIGHT(fight_id),
--    foreign key (fighter_code)
--    references FIGHTER(fighter_code)
-- );

-- create table BLUE_CORNER (
--	age integer,
--	weight float,
--	win_streak integer,
--	wins integer,
--	losses integer,
--	draws integer,
--    fighter_code integer,
--    fight_id integer,
--    foreign key (fight_id)
--    references FIGHT(fight_id),
--    foreign key (fighter_code)
--    references FIGHTER(fighter_code)
-- ;


-- create table RESULT (
--	winner integer,
--	total_fight_seconds integer,
--	total_rounds integer,
--    fight_id integer,
--	primary key (winner, fight_id),
--    foreign key (fight_id)
--    references FIGHT(fight_id),
--    foreign key (winner)
--    references FIGHTER(fighter_code)
-- );



create table WEIGHT_CLASS (
	code integer NOT NULL,
    weight varchar(50),
	primary key (code)
);

create table FIGHTER (
    code integer,
	name varchar(50),
	height float,
	reach float,
	stance varchar(50),
	primary key (code)
);

create table FIGHT (
	code integer UNIQUE,
	referee varchar(50),
	location varchar(50),
	fight_date date,
    weight_class_code integer,
    winner varchar(50),

    age_rc integer,
    weight_rc float,
    win_streak_rc integer,
    wins_rc integer,
    losses_rc integer,
    fighter_rc_code integer,
    fighter_bc_code integer,

    age_bc integer,
    weight_bc float,
    win_streak_bc integer,
    wins_bc integer,
    losses_bc integer,
    -- winner varchar(40), ?
    primary key (code),
    foreign key (weight_class_code)
    references WEIGHT_CLASS(code),
    foreign key (fighter_rc_code)
    references FIGHTER(code),
    foreign key (fighter_bc_code)
    references FIGHTER(code)
);

create table BET (
	amount float,
	code integer UNIQUE,
	date_bet date,
    fight_id integer,
    winner Varchar(50),
    payoff float,
	primary key (code),
    foreign key (fight_id)
    references FIGHT(code),
    CHECK (AMOUNT > 0)
);