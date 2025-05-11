grammar GameGrammar;

program: sentence EOF; // nhận đúng 1 lệnh và đọc hết lệnh.

sentence: defendCommand
        | useHealCommand
        | useSkillDirectionCommand
        | collectCommand
        | attackCommand;

defendCommand: DEFEND DIRECTION;
useHealCommand: USE HEAL;
useSkillDirectionCommand: USE SKILL DIRECTION;
collectCommand: COLLECT BUFF;
attackCommand: ATTACK DIRECTION ID;

// action:
DEFEND: 'defend';
USE: 'use';
COLLECT: 'collect';
ATTACK: 'attack';

DIRECTION: 'left' | 'mleft' | 'mid' | 'mright' | 'right';
SKILL: 'laser' |'freeze';
HEAL: 'heal';
BUFF: 'laserP' | 'freezeP';

ID: [A-Za-z]+;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines