package com.persistance.service;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;






import com.persistance.dao.IUtilisateurDao;
import com.persistance.model.Utilisateur;


@Service
@Transactional
public class UtilisateurService {

    @Autowired
    private IUtilisateurDao dao;

    public UtilisateurService() {
    	//  super();
    }

    // API

    public void create(final Utilisateur entity) {
    	System.out.println("dao "+dao);
    	System.out.println(entity);
        dao.create(entity);
    }
    
    public void delete(final Utilisateur entity) {
    
    	System.out.println(entity);
        dao.delete(entity);
    }

    public void update(final Utilisateur entity) {
        
    	System.out.println(entity);
        dao.update(entity);
    }
    public List<Utilisateur> findAll() {
    	
    	 List<Utilisateur> l= dao.findAll();
    		System.out.println("count "+l.size());
     return  l;
    }
    
    public List<Utilisateur> findbyloginndpwd(String userName,String pwd) {
    //  private String userName;
   //     private String password;
        	
   	 List<Utilisateur> l= dao.findByCriteria(userName, pwd ,"userName", "password");
   		System.out.println("count "+l.size());
    return  l;
   }
}
