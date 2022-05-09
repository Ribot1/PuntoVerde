--2. SP agregar usuario
-----------------------
CREATE OR REPLACE PROCEDURE sp_agregar_usuario( username IN  AUTH_USER.username%TYPE,
                                                first_name IN  AUTH_USER.first_name%TYPE,
                                                last_name IN  AUTH_USER.last_name%TYPE,
                                                email IN  AUTH_USER.email%TYPE,
                                                password IN  AUTH_USER.password%TYPE,
                                                v_salida OUT NUMBER
                                                )
IS

BEGIN
    INSERT INTO AUTH_USER(username, first_name, last_name, email, password)
    VALUES(username, first_name, last_name, email, password);
    COMMIT;
    v_salida:=1;
    
EXCEPTION
    WHEN OTHERS THEN
    v_salida:=0;
    
END;


------------------------
--3. SP eliminar usuario
------------------------
CREATE OR REPLACE PROCEDURE sp_eliminar_usuario(ID int,
                                                a_id int,
                                                v_salida OUT NUMBER
                                                )
IS

BEGIN
	DELETE AUTH_USER WHERE a_id = ID;
    COMMIT;
    v_salida:=1;
    
EXCEPTION
    WHEN OTHERS THEN
    v_salida:=0;
    
END;

-------------------------
--4. SP modificar usuario
-------------------------
CREATE OR REPLACE PROCEDURE sp_agregar_usuario( username IN  AUTH_USER.username%TYPE,
                                                first_name IN  AUTH_USER.first_name%TYPE,
                                                last_name IN  AUTH_USER.last_name%TYPE,
                                                email IN  AUTH_USER.email%TYPE,
                                                password IN  AUTH_USER.password%TYPE,
                                                v_salida OUT NUMBER
                                                )
IS

BEGIN
	UPDATE AUTH_USER SET  a_username    = username,
                            nombre      = first_name,
                            apellido    = last_name,
                            correo      = email,
                            clave       = password
                        WHERE id = p_id;
    COMMIT;
    v_salida:=1;

EXCEPTION
    WHEN OTHERS THEN
    v_salida:=0;

END;
