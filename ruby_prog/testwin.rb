require 'java'  
include_class(['javax.swing.JFrame','javax.swing.JLabel','javax.swing.JComboBox','javax.swing.JButton','javax.swing.JPanel','javax.swing.JTable','javax.swing.JTextField', 
'java.awt.GridBagLayout', 'java.awt.GridBagConstraints'])
          window= JFrame.new         
          contentPane = window.getContentPane         
          gridbag = GridBagLayout.new         
          contentPane.setLayout gridbag                  
          c = GridBagConstraints.new          
          #setting a default constraint value         
          c.fill = GridBagConstraints::HORIZONTAL             
          tagLbl = JLabel.new("Tags")         
          c.gridx = 0          
          c.gridy = 0          
          gridbag.setConstraints tagLbl, c          
          contentPane.add(tagLbl)                  
          tagModeLbl = JLabel.new("Tag Mode")         
          c.gridx = 0         
          c.gridy = 1         
          gridbag.setConstraints(tagModeLbl, c)         
          contentPane.add(tagModeLbl)                  
          tagTxt = JTextField.new("plinth")         
          c.gridx = 1         
          c.gridy = 0         
          c.gridwidth = 2         
          gridbag.setConstraints(tagTxt, c)         
          contentPane.add(tagTxt)                  
          modeCombo = JComboBox.new         
          modeCombo.addItem "all"         
          modeCombo.addItem "any"         
          c.gridx = 1         
          c.gridy = 1         
          c.gridwidth = 1         
          gridbag.setConstraints(modeCombo, c)         
          contentPane.add(modeCombo)                  
          searchBtn = JButton.new("Search")         
          c.gridx = 1         
          c.gridy = 2         
          gridbag.setConstraints(searchBtn, c)         
          contentPane.add(searchBtn)          
          resTable = JTable.new(5,3)         
          c.gridx = 0         
          c.gridy = 3         
          c.gridwidth = 3         
          gridbag.setConstraints(resTable, c)         
          contentPane.add(resTable)                  
          previewLbl = JLabel.new("Preview goes here")         
          c.gridx = 0         
          c.gridy = 4         
          gridbag.setConstraints(previewLbl, c)         
          contentPane.add(previewLbl)                  
          window.defaultCloseOperation = JFrame::EXIT_ON_CLOSE                  
          window.pack()         
          window.setVisible(true) 
          
